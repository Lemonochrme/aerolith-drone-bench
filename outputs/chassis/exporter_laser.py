"""Export du prototype MDF 4 mm, sans dégagements de fraise."""
from pathlib import Path
import argparse, ast, json, subprocess, sys

O = Path(__file__).resolve().parent

def placements():
    result = [('01_Platine_centrale', x, 160) for x in (85, 235)]
    for y in (360, 405, 450, 495):
        result += [('02_Bras_court', 100, y), ('03_Bras_long', 315, y)]
    result += [('04_Socle_moteur', x, y) for x in (370, 460) for y in (65, 145, 225, 305)]
    return result + [('05_Coupon_ajustement', 458, 455)]

def geometry():
    import FreeCAD as App
    import Part
    source = (O / 'construire.FCMacro').read_text(encoding='utf-8')
    ns = {'__file__': str(O / 'construire.FCMacro'), 'LASER': True}
    exec(source.split('# Native FreeCAD project')[0], ns)
    node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef) and n.name == 'contour_data')
    exec(ast.get_source_segment(source, node), ns)
    forms = ns['forms']
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
    (O / '.build').mkdir(exist_ok=True)
    (O / '.build/laser-contours.json').write_text(json.dumps(data), encoding='utf-8')
    print(f'19 pieces / espacement minimum {gap:.3f} mm / contours valides')

def export(freecad_python):
    import ezdxf
    subprocess.run([freecad_python, str(Path(__file__).resolve()), '--geometry'], check=True)
    data = json.loads((O / '.build/laser-contours.json').read_text())
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
            for c in data[key]:
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

    write('MDF4_600x600.dxf', placements())
    write('Coupon_MDF4.dxf', [('05_Coupon_ajustement', 42, 21)])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--geometry', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('--freecad-python', default=r'C:\Program Files\FreeCAD 1.1\bin\python.exe')
    args = parser.parse_args()
    if args.geometry:
        geometry()
    else:
        export(args.freecad_python)
