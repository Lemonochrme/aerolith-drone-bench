import FreeCAD as App,FreeCADGui as Gui,math,time,json
from pathlib import Path
D=App.ActiveDocument;S=D.Parametres
frames=Path(r'C:\Users\robin\Documents\Codex\2026-10-16\d-veloppe-un-banc-de-calibration-7\work\video_v5_4k');frames.mkdir(exist_ok=True)
v=Gui.activeDocument().activeView();v.viewAxonometric();v.setCameraType('Orthographic');v.fitAll();cam=v.getCameraNode();cam.height.setValue(1750)
initial=tuple(cam.position.getValue());camera=v.getCamera();start=time.time()
try:
 for i in range(288):
  t=i/24
  if t<3:
   u=t/3;y=95*math.sin(math.pi*u)**2;p=r=0
  elif t<6:
   u=(t-3)/3;p=75*math.sin(2*math.pi*u)*math.sin(math.pi*u);y=r=0
  elif t<9:
   u=(t-6)/3;r=75*math.sin(2*math.pi*u)*math.sin(math.pi*u);y=p=0
  else:
   u=(t-9)/3;e=math.sin(math.pi*u)**2;y=65*math.sin(2*math.pi*u)*e;p=45*math.sin(2*math.pi*u)*e;r=55*math.sin(2*math.pi*u+.7)*e
  for cell,val in zip(['B4','B5','B6'],[y,p,r]):S.set(cell,str(val))
  D.recompute();Gui.updateGui();v.saveImage(str(frames/('%04d.png'%i)),3840,2160,'White')
  if i%12==0:(frames/'progress.json').write_text(json.dumps({'frame':i,'total':288,'elapsed':round(time.time()-start,1)}))
finally:
 for c in ['B4','B5','B6']:S.set(c,'0')
 D.recompute();v.setCamera(camera)
(frames/'complete.json').write_text(json.dumps({'frames':288,'fps':24,'resolution':[3840,2160],'elapsed':time.time()-start}))
print('Video frames complete')

