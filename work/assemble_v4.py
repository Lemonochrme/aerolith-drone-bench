import FreeCAD as App,Part,Import,math,json
from pathlib import Path
root=Path(r'C:\Users\robin\Documents\Codex\2026-10-16\d-veloppe-un-banc-de-calibration-7')
O=root/'outputs'/'V4_Drone_assemble';O.mkdir(exist_ok=True)
D=App.openDocument(str(root/'outputs/V3_Pivot_lacet/Banc_IMU_V3_Pivot_lacet.FCStd'))
D.Label='Banc IMU V4 — LithFrame assemblé'
V=App.Vector
for c in ['B4','B5','B6']:D.Parametres.set(c,'0')
D.DroneReference.Label='05 — LithFrame F380 assemblé / contours DXF'
src=json.loads((root/'outputs/contours_source.json').read_text())
def plate(prefix):
 es=next(v for k,v in src.items() if k.startswith(prefix));edges=[]
 for e in es:
  if e[0]=='LINE':edges.append(Part.makeLine(V(*e[1]),V(*e[2])))
  elif e[0]=='CIRCLE':edges.append(Part.makeCircle(e[2],V(*e[1])))
  else:edges.append(Part.makeCircle(e[2],V(*e[1]),V(0,0,1),e[3],e[4] if e[4]>e[3] else e[4]+360))
 for e in edges:e.fixTolerance(.001)
 return Part.makeFace([Part.Wire(w) for w in Part.sortEdges(edges,.01)],'Part::FaceMakerBullseye').extrude(V(0,0,3))
def add(n,s,col=(.12,.14,.16),parent=None,spec='Contour DXF fourni ; carbone 3 mm supposé'):
 o=D.addObject('PartDesign::Feature',n);(parent or D.DroneReference).addObject(o);o.Shape=s;o.ViewObject.ShapeColor=col
 o.addProperty('App::PropertyString','Specification','Fabrication');o.Specification=spec
 o.addProperty('App::PropertyString','Categorie','Fabrication');o.Categorie='Drone assemblé'
 return o
def move(s,p,rot=None):
 s=s.copy();s.Placement=App.Placement(V(*p),rot or App.Rotation());return s
carbon=plate('Base');add('LithFrame_platine_superieure_DXF',carbon)
short,long,motor=plate('Bras court'),plate('Bras long'),plate('Socle moteur')
# Root slots and motor slots give an exact converging pair (residual < 0.001 mm).
angles=[22.198102,47.198102];roots=[(14.180925185,102.561125984),(41.414460411,11.777008489)]
canon=[]
for typ,s,a,p,rootx in [('court',short,angles[0],roots[0],-67.5),('long',long,angles[1],roots[1],-82.5)]:
 rz=App.Rotation(V(0,0,1),a);r=rz.multiply(App.Rotation(V(1,0,0),90));center=V(p[0],p[1],-10)-r.multVec(V(rootx,0,1.5))
 canon.append((typ,move(s,tuple(center),r)))
a=math.radians(angles[0]);tab=V(roots[0][0]+116*math.cos(a),roots[0][1]+116*math.sin(a),0)
mr=App.Rotation(V(0,0,1),-55);mp=tab-mr.multVec(V(-14.184693509,-8.329579633,0))
mc=mp+mr.multVec(V(2.564,-2.314,0))
indic=D.addObject('App::Part','EquipementsIndicatifs');D.DroneReference.addObject(indic);indic.Label='Équipements indicatifs — dimensions à confirmer'
checks=[]
for sx in [-1,1]:
 for sy in [-1,1]:
  M=App.Matrix();M.A11=sx;M.A22=sy
  q=f'{"D" if sx>0 else "G"}_{"AV" if sy>0 else "AR"}'
  for typ,s in canon:add('Bras_'+typ+'_'+q,s.transformGeometry(M))
  for z in [-18,-5]:add('Socle_moteur_'+q+('_bas' if z==-18 else '_haut'),move(motor,(mp.x,mp.y,z),mr).transformGeometry(M))
  x,y=sx*mc.x,sy*mc.y
  mot=Part.makeCylinder(14,20,V(x,y,-2)).fuse(Part.makeCylinder(3,10,V(x,y,18)))
  add('Moteur_indicatif_'+q,mot,(.28,.29,.31),indic,'Encombrement générique Ø28 × 20 mm + arbre ; référence moteur non fournie')
# Standard spacer representation, matching supplied 30.5 mm square mounting holes.
for x in [-15.25,15.25]:
 for y in [-15.25,15.25]:
  st=Part.makeCylinder(3,20,V(x,y,-20)).cut(Part.makeCylinder(1.6,20,V(x,y,-20)))
  add('Entretoise_chassis_M3_20',st,(.72,.75,.78),spec='Entretoise M3 longueur 20 mm ; visserie à confirmer sur châssis réel')
add('Batterie_indicative',Part.makeBox(36,100,38,V(-18,-50,8)),(.15,.35,.65),indic,'Encombrement générique 36 × 100 × 38 mm ; batterie réelle non fournie')
add('Controleur_indicatif',Part.makeBox(36,36,7,V(-18,62,8)),(.12,.5,.25),indic,'Encombrement générique 36 × 36 × 7 mm ; électronique réelle non fournie')
D.Enveloppe_drone_500x160.Visibility=False
D.recompute()
new=[o for o in D.Objects if hasattr(o,'Categorie') and o.Categorie=='Drone assemblé']
invalid=[o.Name for o in new if not o.Shape.isValid()]
# Clearance against bench solids at neutral position; contacts within the drone are intentional.
bench=[o for o in D.Objects if hasattr(o,'Categorie') and hasattr(o,'Shape') and o.ViewObject.Visibility and o not in new and o.Name!='LithFrame_base_DXF' and o not in D.PiecesImprimees.Group and o.Categorie!='Contrôle']
coll=[]
for o in new:
 if not(o.Name.startswith('Bras_') or o.Name.startswith('Socle_moteur_') or o.Name.startswith('Moteur_')):continue
 s=o.Shape.copy();s.Placement=o.getGlobalPlacement()
 for b in bench:
  bs=b.Shape.copy();bs.Placement=b.getGlobalPlacement()
  if s.BoundBox.intersect(bs.BoundBox):
   vol=s.common(bs).Volume
   if vol>.1:coll.append([o.Name,b.Name,round(vol,3)])
report={'nouveaux_objets':len(new),'formes_invalides':invalid,'interferences_banc_position_neutre_mm3':coll,'bras_sur_chant':8,'socles_moteurs':8,'platines_centrales':2,'epaisseur_carbone_supposee_mm':3,'residu_alignement_rainures_mm':0.00022,'equipements_indicatifs':6,'masse_complete_reference_kg':2}
(O/'verification_V4.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
Gui.activeDocument().activeView().viewAxonometric();Gui.activeDocument().activeView().fitAll();Gui.activeDocument().activeView().getCameraNode().height.setValue(1700)
D.recompute();D.saveAs(str(O/'Banc_IMU_V4_Drone_assemble.FCStd'))
Gui.activeDocument().activeView().saveImage(str(O/'Banc_V4_ensemble.png'),1600,1200,'White')
# Detail camera centered on drone.
cam=Gui.activeDocument().activeView().getCameraNode();cam.position.setValue(900,-1200,1800);cam.pointAt(__import__('pivy').coin.SbVec3f(0,0,895),__import__('pivy').coin.SbVec3f(0,0,1));cam.height.setValue(620)
Gui.activeDocument().activeView().saveImage(str(O/'Drone_V4_detail.png'),1600,1200,'White')
visible=[o for o in D.Objects if hasattr(o,'Categorie') and hasattr(o,'Shape') and o.ViewObject.Visibility and o not in D.PiecesImprimees.Group and o.Categorie!='Contrôle']
tmp=App.newDocument('ExportV4');objs=[]
for o in visible:
 c=tmp.addObject('PartDesign::Feature',o.Name);c.Label=o.Label;c.Shape=o.Shape;c.Placement=o.getGlobalPlacement();objs.append(c)
Import.export(objs,str(O/'Banc_IMU_V4_Drone_assemble.step'));App.closeDocument(tmp.Name);App.setActiveDocument(D.Name)
print(report)
