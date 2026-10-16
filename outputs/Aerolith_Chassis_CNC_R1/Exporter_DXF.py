from pathlib import Path
import json,math,csv,ezdxf
O=Path(__file__).resolve().parent;data=json.loads((O/'contours_CNC.json').read_text())
qty={'01_Platine_centrale':2,'02_Bras_court':4,'03_Bras_long':4,'04_Socle_moteur':8,'05_Coupon_ajustement':1}
def setup():
 d=ezdxf.new('R2010');d.units=4
 for n,col in [('DECOUPE',7),('ANNOTATIONS_NE_PAS_USINER',3),('PLAQUE_REFERENCE',8)]:d.layers.new(n,dxfattribs={'color':col})
 return d
def insert(ms,key,dx=0,dy=0):
 for c in data[key]:
  if c['type']=='CIRCLE':ms.add_circle((c['center'][0]+dx,c['center'][1]+dy),c['radius'],dxfattribs={'layer':'DECOUPE'})
  else:ms.add_lwpolyline([(x+dx,y+dy,b) for x,y,b in c['points']],format='xyb',close=True,dxfattribs={'layer':'DECOUPE'})
for key in data:
 d=setup();insert(d.modelspace(),key);d.saveas(O/'DXF'/(key+'.dxf'))
 d2=ezdxf.readfile(O/'DXF'/(key+'.dxf'));errors=d2.audit();assert not errors.errors
 ms=d2.modelspace();assert all(e.dxftype()=='CIRCLE' or e.closed for e in ms)
placements=[]
for x in [85,235]:placements.append(['01_Platine_centrale',x,160])
for y in [350,393,436,479]:placements.extend([['02_Bras_court',100,y],['03_Bras_long',315,y]])
for x in [365,440]:
 for y in [65,140,215,290]:placements.append(['04_Socle_moteur',x,y])
placements.append(['05_Coupon_ajustement',458,455])
d=setup();ms=d.modelspace();ms.add_lwpolyline([(0,0),(600,0),(600,600),(0,600)],close=True,dxfattribs={'layer':'PLAQUE_REFERENCE'})
for i,(key,x,y) in enumerate(placements):
 insert(ms,key,x,y)
 ms.add_text(f'{i+1:02d} {key[:2]}',dxfattribs={'layer':'ANNOTATIONS_NE_PAS_USINER','height':3}).set_placement((x,y))
ms.add_text('CARBONE 4 mm / FRAISE 3 mm / CONTOURS NOMINAUX',dxfattribs={'layer':'ANNOTATIONS_NE_PAS_USINER','height':5}).set_placement((25,565))
ms.add_text('REFERENCE 600 x 600 / HORS COMPENSATION, PONTS ET PARCOURS CAM',dxfattribs={'layer':'ANNOTATIONS_NE_PAS_USINER','height':4}).set_placement((25,550))
d.saveas(O/'DXF/Planche_600x600_quantites_completes.dxf')
(O/'implantation_planche.json').write_text(json.dumps(placements,indent=2),encoding='utf-8')
with (O/'Nomenclature_chassis_CNC.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['Pièce','Quantité','Matière','Épaisseur_mm','Notes'])
 for k,q in qty.items():w.writerow([k,q,'Carbone',4,'Coupon à tester avant les pièces finales' if 'Coupon' in k else 'Contour DXF nominal'])
 w.writerow(['Entretoise M3 L20',4,'Métal','','Centrale, dimensions à confirmer'])
 w.writerow(['Entretoise M3 L10',12,'Métal','','Trois par support moteur double'])
 w.writerow(['Visserie M3 de fermeture','','Acier','','Longueurs selon entretoises et écrous achetés ; non détaillée dans la CAO'])
print('DXF exportés :',len(data)+1,'; pièces sur planche :',len(placements))
