# MDF 3 mm, CNC fraise Ø3 mm

[Cadre complet 600 × 600](MDF3_CNC_fraise3_600x600.dxf) | [Coupon et témoin](Coupon_MDF3_CNC_fraise3.dxf) | [Plan des T-bones](Plan_Tbone_fraise3.pdf)

18 pièces : 2 platines, 4 bras courts avec pieds, 4 bras longs et 8 socles moteur. DXF en mm, échelle 1:1, calque DECOUPE. Contours nominaux sans compensation de fraise ni parcours FAO.

Mortaises nominales : 14,08 × 3,05 aux racines ; 12,08 × 3,05 aux moteurs. Quatre T-bones par mortaise, perpendiculaires aux grands côtés, de rayon 1,525 pour le MDF 3 mm. Largeur totale avec dégagements : 6,10. Les épaulements des tenons ont des T-bones de rayon 1,6 dirigés vers l’extérieur du tenon. Les tenons gardent leurs largeurs de 14 et 12 et leur profondeur de 3.

Les quatre lumières inutilisées de 22 × 7 sont supprimées. Sangles de batterie, colliers ESC, perçages de fixation et perçage moteur à diagonales de 19 sont conservés. Le FreeCAD et le STEP du dossier parent représentent le carbone de 4 mm.

Tester le coupon dans la même plaque. Largeurs nominales : 3,000 / 3,025 / 3,050 / 3,075 / 3,100 / 3,150. Le cadre utilise 3,050. Mesurer l’épaisseur réelle et vérifier le témoin avant le cadre. Bridage, ponts, compensation et passes restent à définir en FAO. La résistance aux chocs et au vol n’est pas validée.

Reconstruction : `python exporter_laser.py --cnc --thickness 3 --slot-clearance 0.05`.
