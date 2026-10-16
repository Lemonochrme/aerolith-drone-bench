import FreeCAD as App,Part,Import
from pathlib import Path
O=Path(r'C:\Users\robin\Documents\Codex\2026-10-16\d-veloppe-un-banc-de-calibration-7\outputs\V5_Helices_4K')
d=App.openDocument(str(O/'Banc_IMU_V5_Helices.FCStd'));t=App.newDocument('Export');objects=[]
for o in d.Objects:
 if hasattr(o,'Categorie') and hasattr(o,'Shape') and o.Visibility and o not in d.PiecesImprimees.Group and o.Categorie!='Contrôle':
  c=t.addObject('PartDesign::Feature',o.Name);c.Shape=o.Shape;c.Placement=o.getGlobalPlacement();objects.append(c)
Import.export(objects,str(O/'Banc_IMU_V5_Helices.step'))
print('STEP',len(objects))
