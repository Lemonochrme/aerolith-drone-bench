from pathlib import Path
import json,math,csv,ezdxf
O=Path(__file__).resolve().parent;data=json.loads((O/'.build/contours.json').read_text())
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
 d=setup();insert(d.modelspace(),key);d.saveas(O/'dxf'/(key+'.dxf'))
 d2=ezdxf.readfile(O/'dxf'/(key+'.dxf'));errors=d2.audit();assert not errors.errors
 ms=d2.modelspace();assert all(e.dxftype()=='CIRCLE' or e.closed for e in ms)
placements=[]
for x in [85,235]:placements.append(['01_Platine_centrale',x,160])
for y in [360,405,450,495]:placements.extend([['02_Bras_court',100,y],['03_Bras_long',315,y]])
for x in [370,460]:
 for y in [65,145,225,305]:placements.append(['04_Socle_moteur',x,y])
placements.append(['05_Coupon_ajustement',458,455])
d=setup();ms=d.modelspace();ms.add_lwpolyline([(0,0),(600,0),(600,600),(0,600)],close=True,dxfattribs={'layer':'PLAQUE_REFERENCE'})
for i,(key,x,y) in enumerate(placements):
 insert(ms,key,x,y)
 ms.add_text(f'{i+1:02d} {key[:2]}',dxfattribs={'layer':'ANNOTATIONS_NE_PAS_USINER','height':3}).set_placement((x,y))
ms.add_text('CARBONE 4 mm / FRAISE 3 mm / CONTOURS NOMINAUX',dxfattribs={'layer':'ANNOTATIONS_NE_PAS_USINER','height':5}).set_placement((25,565))
ms.add_text('REFERENCE 600 x 600 / HORS COMPENSATION, PONTS ET PARCOURS CAM',dxfattribs={'layer':'ANNOTATIONS_NE_PAS_USINER','height':4}).set_placement((25,550))
d.saveas(O/'dxf/Planche_600x600_quantites_completes.dxf')
(O/'.build/implantation.json').write_text(json.dumps(placements,indent=2),encoding='utf-8')
with (O/'composants.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['Piece','Quantite','Matiere','Dimension','Notes'])
 for k,q in qty.items():w.writerow([k,q,'Carbone','4 mm','Coupon a tester avant les pieces finales' if 'Coupon' in k else 'Contour DXF nominal'])
 for row in [
 ['Entretoise racine M3',16,'Metal','L20 / Øext6','Entre les deux platines centrales'],
 ['Entretoise moteur M3',20,'Metal','L16 / Øext6','Cinq par paire de socles'],
 ['Entretoise centrale M4',4,'Metal','L20 / Øext8','Fermeture structurelle, independante de la FC'],
 ['Vis M3x35',16,'Acier','','Fermeture des racines'],
 ['Vis M3x30',20,'Acier','','Fermeture des supports moteur'],
 ['Vis M3x20',4,'Acier','','Fixation FC ; longueur a ajuster au montage souple reel'],
 ['Vis M3x8',16,'Acier','','Moteurs ; longueur et profondeur de vissage a confirmer'],
 ['Ecrou frein M3',40,'Acier','','Racines, supports et FC ; ne pas compter les filetages moteurs'],
 ['Rondelle M3',96,'Acier','','Deux par fixation avec ecrou, une par vis moteur'],
 ['Vis M4x40',4,'Acier','','Fermeture centrale'],['Ecrou frein M4',4,'Acier','','Fermeture centrale'],['Rondelle M4',8,'Acier','','Fermeture centrale'],
 ['Support souple FC',4,'Silicone','L7 / passage M3','Encombrement provisoire'],
 ['FC',1,'Electronique','Entraxe 30.5x30.5','Carte et composants generiques ; modele exact non fourni'],
 ['ESC',4,'Electronique','50x18x8','Reference non choisie ; dimensions provisoires hors cables'],
 ['Collier ESC',4,'Nylon','2.5x100','Passages integres dans les platines'],
 ['Adhesif isolant ESC',4,'Isolant','50x18x2','Montage provisoire'],
 ['GTSkytenRC 3115 640KV',4,'Moteur','Enveloppe Ø38 / corps33 / arbre M5','Pas de plan fabricant disponible ; verifier le percage 19x19 et le passage central Ø9'],
 ['Helice tripale 9x5x3',4,'Helice','Ø228.6 / pas127','Deux de chaque sens ; forme simplifiee, pas une CAO constructeur'],
 ['Ecrou helice M5',4,'Metal','','Avec le moteur si fourni ; type et longueur utile a confirmer'],
 ['Rondelle helice M5',4,'Metal','','Selon fixation fournie avec le moteur'],
 ['Batterie',1,'Batterie','148x44x52','Reference non choisie ; volume provisoire sans tension ni capacite imposee'],
 ['Pad batterie',1,'Isolant','140x40x7','Provisoire'],['Sangle batterie',2,'Textile','Largeur20','Longueur selon batterie reelle']
 ]:w.writerow(row)
print('DXF : cinq pieces et planche ; composants mis a jour')
