# Banc IMU

Socle de 1000 × 1000 mm. Axes du cardan à 895 mm du socle. Charge de conception : drone complet de 2 kg.

[FreeCAD](banc.FCStd) | [STEP](banc.step) | [Composants et quantités](composants.csv)

[STL](stl/) : 25 pièces montées, un coupon et un gabarit. Chaque pièce tient sur 220 × 220 mm.

[Plans de structure](plans/structure.dxf) : goussets CP03, platine CP04 et ponts AL01.

[Plans du pivot](plans/pivot.dxf) : panneaux CP05/CP06 et plaques AL02 à AL05.

[Montage](montage.md)

Profilés Type B, rainure 8. Les vis et écrous sont détaillés dans le CSV. Les entretoises et la visserie du drone sont distinctes de celles du banc.

Dans FreeCAD, les cellules B4, B5 et B6 du tableau Parametres pilotent le lacet, le tangage et le roulis.

Le drone affiché utilise le châssis LithFrame d'origine. Moteurs, électronique et hélices sont des volumes indicatifs. Le châssis CNC est un projet séparé.

Usage prévu : poses manuelles statiques, hélices retirées sur le drone réel. Résistance sous charge et essais moteurs non validés.
