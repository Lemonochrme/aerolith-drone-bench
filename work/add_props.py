import FreeCAD as App,Part,math,json
from pathlib import Path
root=Path(r'C:\Users\robin\Documents\Codex\2026-10-16\d-veloppe-un-banc-de-calibration-7');O=root/'outputs/V5_Helices_4K';O.mkdir(exist_ok=True)
D=App.openDocument(str(root/'outputs/V4_Drone_assemble/Banc_IMU_V4_Drone_assemble.FCStd'));D.Label='Banc IMU V5 — drone avec hélices'
V=App.Vector
for cell in ['B4','B5','B6']:D.Parametres.set(cell,'0')
props=D.addObject('App::Part','HelicesIndicatives');D.DroneReference.addObject(props);props.Label='Hélices bipales 9 pouces — géométrie indicative'
def blade(sign):
 sections=[]
 for x,w,a in [(8,7,30),(20,16,24),(52,21,15),(86,16,10),(108,8,7),(114.3,1,6)]:
  t=1.4;r=App.Rotation(V(1,0,0),sign*a)
  pts=[V(x,0,0)+r.multVec(V(0,y,z)) for y,z in [(-w/2,-t/2),(w/2,-t/2),(w/2,t/2),(-w/2,t/2),(-w/2,-t/2)]]
  sections.append(Part.makePolygon(pts))
 return Part.makeLoft(sections,True,False)
for i,m in enumerate([o for o in D.Objects if o.Name.startswith('Moteur_indicatif_')]):
 b=m.Shape.BoundBox;x=(b.XMin+b.XMax)/2;y=(b.YMin+b.YMax)/2;sgn=1 if x*y>0 else -1
 s=blade(sgn);s2=s.copy();s2.rotate(V(),V(0,0,1),180)
 shape=Part.makeCylinder(8.5,4,V(0,0,-2)).fuse(s).fuse(s2).cut(Part.makeCylinder(3.1,10,V(0,0,-5)))
 o=D.addObject('PartDesign::Feature','Helice_'+m.Name.split('indicatif_')[1]);props.addObject(o);o.Shape=shape;o.Placement=App.Placement(V(x,y,24),App.Rotation(V(0,0,1),25 if sgn>0 else -25));o.ViewObject.ShapeColor=(.65,.67,.7)
 o.addProperty('App::PropertyString','Specification','Fabrication');o.Specification='Bipale indicative diamètre 228,6 mm (9 pouces), sens alternés ; référence et pas réels non fournis'
 o.addProperty('App::PropertyString','Categorie','Fabrication');o.Categorie='Drone assemblé'
D.recompute();D.saveAs(str(O/'Banc_IMU_V5_Helices.FCStd'))
v=Gui.activeDocument().activeView();v.viewAxonometric();v.fitAll();Gui.updateGui();v.saveImage(str(O/'Banc_V5_apercu.png'),1920,1080,'White')
print([(o.Name,o.Shape.isValid()) for o in props.Group])
