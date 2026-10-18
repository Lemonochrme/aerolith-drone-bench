# Prototype MDF 4 mm

Châssis R7. Platines centrales de 120 × 250. Socles de 58 × 62, centrés sur les axes moteurs.

[Planche 600 × 600](MDF4_600x600.dxf) | [Coupon seul](Coupon_MDF4.dxf)

DXF R2010, en mm, échelle 1:1. Un seul calque DECOUPE. Aucun texte, cadre, doublon ou tracé de gravure.

La planche contient 2 platines centrales, 4 bras courts, 4 bras longs, 8 socles moteurs et 1 coupon. Le coupon séparé permet un essai avant la planche complète. Espacement minimal entre pièces : 11 mm.

Les dégagements de fraise sont retirés des bras et des mortaises. Les six passages de 8 × 4 servent aux quatre colliers de maintien des ESC. Les emboîtements gardent les cotes nominales du modèle : tenons de 14 et 12, mortaises de 14,08 × 4,05 et 12,08 × 4,05.

Les six mortaises du coupon font, de gauche à droite : 4,000 / 4,025 / 4,050 / 4,075 / 4,100 / 4,150 de large. Tester avec une chute et un tenon de bras dans le MDF réel. Le fichier complet utilise 4,050.

Les contours ne sont pas compensés. Régler la compensation de largeur de coupe dans le logiciel de la machine après mesure sur une chute. Découper les contours intérieurs avant les contours extérieurs. Puissance, vitesse et passes dépendent de la machine et du MDF.

Ce prototype MDF sert à vérifier l'assemblage. Sa résistance pour un vol ou un essai motorisé n'est pas validée. Le fichier ne vaut pas validation d'une découpe laser du carbone.

Reconstruction : exécuter exporter_laser.py avec Python et ezdxf. Le script appelle le Python fourni par FreeCAD ; son chemin peut être passé avec --freecad-python.
