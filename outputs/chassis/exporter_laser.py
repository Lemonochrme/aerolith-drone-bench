"""Export du prototype MDF, épaisseur nominale 3 mm, sans dégagements de fraise."""
from pathlib import Path
import argparse, ast, json, math, subprocess, sys

O = Path(__file__).resolve().parent

def placements():
    result = [('01_Platine_centrale', x, 160) for x in (85, 235)]
    for y in (360, 430, 500, 570):
        result += [('02_Bras_court', 100, y), ('03_Bras_long', 315, y)]
    result += [('04_Socle_moteur', x, y) for x in (370, 460) for y in (65, 145, 225, 305)]
    return result

def geometry(thickness, clearance):
    import FreeCAD as App
    import Part
    source = (O / 'construire.FCMacro').read_text(encoding='utf-8')
    ns = {'__file__': str(O / 'construire.FCMacro'), 'LASER': True,
          'THICKNESS': thickness, 'SLOT_CLEARANCE': clearance}
    exec(source.split('# Native FreeCAD project')[0], ns)
    node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef) and n.name == 'contour_data')
    exec(ast.get_source_segment(source, node), ns)
    forms = ns['forms']
    # Separate male witness: its 14 mm tenon projects by the sheet thickness.
    points = [(-15,-10),(15,-10),(15,10),(7,10),(7,10+thickness),
              (-7,10+thickness),(-7,10),(-15,10)]
    forms['06_Temoin_ajustement'] = Part.Face(Part.makePolygon(
        [App.Vector(x,y,0) for x,y in points + [points[0]]]))
    assert all(f.isValid() and len(f.Faces) == 1 and all(w.isClosed() for w in f.Wires) for f in forms.values())
    assert all(len(forms[n].Wires) == 1 for n in ('02_Bras_court', '03_Bras_long'))
    sheet = []
    for key, x, y in placements():
        f = forms[key].copy()
        f.translate(App.Vector(x, y, 0))
        assert f.BoundBox.XMin > 5 and f.BoundBox.YMin > 5 and f.BoundBox.XMax < 595 and f.BoundBox.YMax < 595
        sheet.append(f)
    gap = min(a.distToShape(b)[0] for i, a in enumerate(sheet) for b in sheet[i + 1:])
    assert gap > 6
    data = {n: ns['contour_data'](f) for n, f in forms.items()}
    for n, f in forms.items():
        for contour, wire in zip(data[n], f.Wires):
            contour['outer'] = wire.isSame(f.OuterWire)
    (O / '.build').mkdir(exist_ok=True)
    (O / '.build/laser-contours.json').write_text(json.dumps(data), encoding='utf-8')
    report = {'epaisseur_mm': thickness, 'jeu_total_mm': clearance,
              'rainure_mm': thickness + clearance,
              'profondeur_tenons_mm': thickness,
              'pieces_chassis': len(sheet), 'espacement_min_mm': gap,
              'formes': {n: {'aire_mm2': f.Area, 'contours': len(f.Wires)}
                         for n, f in forms.items()}}
    (O / '.build/laser-parametres.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(f'{len(sheet)} pieces / epaisseur {thickness:g} / rainures {thickness+clearance:g} / espacement {gap:.3f} mm')

def export(freecad_python, thickness, clearance):
    import ezdxf
    subprocess.run([freecad_python, str(Path(__file__).resolve()), '--geometry',
                    '--thickness', str(thickness), '--slot-clearance', str(clearance)], check=True)
    data = json.loads((O / '.build/laser-contours.json').read_text())
    # Check the motor interface from the generated contours, before writing DXF.
    circles = [c for c in data['04_Socle_moteur'] if c['type'] == 'CIRCLE']
    shaft = next(c for c in circles if abs(c['radius'] - 4.5) < 1e-8)
    holes = [c for c in circles if abs(math.dist(c['center'], shaft['center']) - 9.5) < 1e-8]
    assert len(holes) == 4 and all(abs(c['radius'] - 1.65) < 1e-8 for c in holes)
    distances = sorted(math.dist(a['center'], b['center'])
                       for i, a in enumerate(holes) for b in holes[i+1:])
    assert all(abs(v - 19/math.sqrt(2)) < 1e-8 for v in distances[:4])
    assert all(abs(v - 19) < 1e-8 for v in distances[4:])
    folder = O / 'laser'
    folder.mkdir(exist_ok=True)

    def write(name, items):
        d = ezdxf.new('R2010')
        d.units = 4
        d.header['$MEASUREMENT'] = 1
        d.layers.new('DECOUPE', dxfattribs={'color': 1})
        m = d.modelspace()
        expected = 0
        for key, x, y in items:
            for c in sorted(data[key], key=lambda c: c['outer']):
                attrs = {'layer': 'DECOUPE'}
                if c['type'] == 'CIRCLE':
                    m.add_circle((c['center'][0] + x, c['center'][1] + y), c['radius'], dxfattribs=attrs)
                else:
                    m.add_lwpolyline([(a + x, b + y, bulge) for a, b, bulge in c['points']], format='xyb', close=True, dxfattribs=attrs)
                expected += 1
        path = folder / name
        d.saveas(path)
        check = ezdxf.readfile(path)
        assert not check.audit().errors and check.units == 4
        assert len(check.modelspace()) == expected
        signatures = set()
        for e in check.modelspace():
            assert e.dxf.layer == 'DECOUPE'
            if e.dxftype() == 'LWPOLYLINE':
                assert e.closed
                sig = ('P', tuple(tuple(round(v, 8) for v in p) for p in e.get_points('xyb')))
            else:
                assert e.dxftype() == 'CIRCLE'
                sig = ('C', tuple(e.dxf.center), e.dxf.radius)
            assert sig not in signatures
            signatures.add(sig)
        print(f'{name} : {expected} contours fermes, sans texte ni cadre')

    tag = f'{thickness:g}'.replace('.', 'p')
    write(f'MDF{tag}_600x600.dxf', placements())
    write(f'Coupon_MDF{tag}.dxf', [('05_Coupon_ajustement', 42, 21),
                                 ('06_Temoin_ajustement', 111, 21)])
    # Eight replacement plates on 300 x 150 mm, with at least 5 mm margins.
    cx, cy = 2.563971143, -9.313539946
    write(f'Socles_moteurs_MDF{tag}_D19_x8.dxf',
          [('04_Socle_moteur', 35 + 75*i - cx, 36 + 75*j - cy)
           for j in range(2) for i in range(4)])
    write(f'Bras_courts_avec_pieds_MDF{tag}_x4.dxf',
          [('02_Bras_court', x, y) for y in (55, 125) for x in (90, 270)])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--geometry', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('--freecad-python', default=r'C:\Program Files\FreeCAD 1.1\bin\python.exe')
    parser.add_argument('--thickness', type=float, default=3.0, help='Epaisseur mesuree du MDF, en mm')
    parser.add_argument('--slot-clearance', type=float, default=.05, help='Jeu total des mortaises, en mm')
    args = parser.parse_args()
    if not (1 <= args.thickness <= 6 and 0 <= args.slot_clearance <= .3):
        parser.error('Epaisseur attendue entre 1 et 6 mm et jeu entre 0 et 0.3 mm')
    if args.geometry:
        geometry(args.thickness, args.slot_clearance)
    else:
        export(args.freecad_python, args.thickness, args.slot_clearance)
