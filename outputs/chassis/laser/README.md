# Découpe MDF 3 mm

[Cadre complet, planche 600 × 600](MDF3_600x600.dxf) | [Coupon et témoin](Coupon_MDF3.dxf) | [Plan coté de contrôle, PDF A3](Plan_controle_MDF3.pdf)

Ces fichiers remplacent la version MDF 4 mm. Ils sont destinés à une plaque de 3,00 mm nominal. Le projet FreeCAD carbone de 4 mm reste séparé.

DXF R2010, unités mm, échelle 1:1. Un seul calque DECOUPE, sans texte, cadre ni gravure. Contours intérieurs écrits avant le pourtour de chaque pièce ; conserver cette priorité dans le logiciel laser. Ne pas redimensionner à l'importation.

La planche contient les 18 pièces du cadre : 2 platines centrales, 4 bras courts, 4 bras longs et 8 socles moteurs. Espacement minimal entre pièces : 14,52 mm. Les essais sont dans le DXF séparé.

## Pieds intégrés

[4 bras courts avec pieds, MDF 3 mm](Bras_courts_avec_pieds_MDF3_x4.dxf)

Un pied par bras court, découpé dans la même pièce. Les quatre bras longs et tous les emboîtements sont conservés. Les quatre bras de remplacement tiennent dans 360 × 150 mm. Appuis à 45 mm sous l’axe des bras, soit 32 mm sous la platine basse, hors visserie. Les raccords extérieurs des pieds ont un rayon de 4 mm ; la semelle rectiligne mesure environ 13,90 mm. Le MDF et ses pieds ne sont pas validés pour les chocs d’atterrissage.

## Socles de remplacement

[8 socles corrigés, MDF 3 mm](Socles_moteurs_MDF3_D19_x8.dxf) | [Plan des socles et gabarit moteur à taille réelle](Plan_socles_MDF3_D19.pdf)

Les huit pièces tiennent dans 300 × 150 mm. Socles R9 de 56 × 61 mm, contre 58 × 62 mm en R8. Le contour est réduit ; les mortaises, perçages moteur et quatre fixations de fermeture sont conservés. Distance minimale des découpes intérieures au bord : 3,51 mm. Le cadre complet et le plan de contrôle intègrent aussi cette correction.

Les quatre lumières inutilisées de 22 × 7 à X = ±10, Y = ±79 sont supprimées des deux platines en R11. Les passages utilisés par les sangles et colliers sont conservés. Les T-bones concernent les [exports CNC](../cnc_mdf3/README.md).

## Emboîtements

- Épaisseur et profondeur des tenons : 3,00 mm.
- Mortaises centrales : 14,08 × 3,05 mm, pour des tenons de longueur 14 mm.
- Mortaises moteur : 12,08 × 3,05 mm, pour des tenons de longueur 12 mm.
- Jeu nominal total en épaisseur : 0,05 mm, avant effet du trait laser.
- Aucun dégagement de fraise sur les bras ou les mortaises.

Les entretoises restent de 20 mm au centre et 16 mm aux moteurs. Les empilages extérieurs passent respectivement à 26 et 22 mm. Les quatre vis de fermeture M3×30 par support et les vis M3×35 aux racines gardent une longueur suffisante. Utiliser des rondelles, sans écraser le MDF.

Les axes moteurs, entraxes, profils pleins des bras longs, supports centrés et quatre fixations par support sont conservés. Perçage GTSkytenRC 3115 corrigé : quatre trous Ø3,3, diagonales de 19 mm, côtés de 13,435 mm. Les centres sont à X/Y = ±6,717514 mm de l’axe moteur. Une vis moteur traverse désormais 1 mm de matière en moins : sa pénétration augmente de 1 mm à longueur identique.

## Essai avant la planche

Le coupon et son témoin mâle tiennent dans une chute de 130 × 45 mm. Les six mortaises, de gauche à droite, font 3,000 / 3,025 / 3,050 / 3,075 / 3,100 / 3,150 mm. Le témoin possède un tenon de 14 mm de long et 3 mm de profondeur ; son épaisseur est celle du MDF réel. Son corps fait 30 mm de large pour contrôler l'échelle et le trait de coupe.

Le cadre utilise la troisième largeur, 3,050 mm. Découper d'abord ce coupon dans la même plaque, avec les mêmes réglages que le cadre. Le témoin doit entrer dans cette troisième mortaise sans forcer et sans jeu excessif. Si ce n'est pas le cas, corriger la compensation du trait laser ou adapter les cotes avant de découper la planche.

Les fichiers ne contiennent aucune compensation de trait laser. L'épaisseur réelle et le trait doivent être mesurés ; un jeu nominal de 0,05 mm n'est pas une précision de fabrication garantie. Puissance, vitesse et passes dépendent de la machine et du MDF.

## Contrôles effectués

Réimportation des deux DXF : 18 faces valides pour le cadre et 2 pour les essais. Vérification des 48 mortaises de largeur 3,05 mm. Assemblage 3D de 18 pièces de 3 mm avec 36 entretoises, sans chevauchement. Profondeur des tenons et engagement dans les deux platines vérifiés.

Ces contrôles valident la géométrie d'assemblage. La résistance du MDF 3 mm pour un vol ou un essai motorisé n'est pas validée.

Reconstruction : `python exporter_laser.py --thickness 3 --slot-clearance 0.05`. Le script utilise ezdxf et le Python de FreeCAD ; son chemin peut être passé avec `--freecad-python`.
