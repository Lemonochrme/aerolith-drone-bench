# Châssis CNC

Carbone de 4 mm. Fraise Ø3 mm. Révision R2. Dimensions en mm.

[FreeCAD](chassis.FCStd) | [STEP](chassis.step) | [DXF](dxf/) | [Composants](composants.csv)

## Liaisons

Les bras sont pleins, avec seulement deux trous Ø3,3 pour leur serrage transversal.

Les tenons mesurent 14 de long aux racines et 12 côté moteur. Les mortaises font respectivement 14,08 × 4,05 et 12,08 × 4,05, avec des dégagements de fraise localisés aux coins. Le jeu nominal total en épaisseur est de 0,05.

Chaque racine reçoit deux équerres métalliques et chaque extrémité de bras côté moteur en reçoit une. Les vis M3 traversent les bras. Les vis verticales serrent les platines et les équerres autour d'entretoises métalliques. Le maintien ne repose donc pas uniquement sur l'ajustement des tenons.

Les 24 équerres sont faites en cornière aluminium 15 × 15 × 2, coupée à 18. Un coin de semelle est recoupé à 10 × 10 pour dégager les équerres voisines et les ESC. Les deux perçages Ø3,3 sont cotés dans le [plan 06](dxf/06_Corniere_percages.dxf).

Espacement intérieur des platines centrales : 20. Espacement intérieur des supports moteurs : 16. Entretoises et visserie détaillées dans le CSV. Les vis et écrous sont simplifiés dans la CAO ; les rondelles sont comptées dans le CSV.

## Pièces carbone

| Pièce | Quantité | Dimensions |
|---|---:|---|
| Platine centrale | 2 | 128 × 270 × 4 |
| Bras court | 4 | 160 × 28 × 4 |
| Bras long | 4 | 190 × 28 × 4 |
| Socle moteur | 8 | 70 × 68 × 4 |
| Coupon d'ajustement | 1 | 84 × 32 × 4 |

## Équipements

La FC et les quatre ESC sont placés entre les platines. Les fixations structurelles centrales sont indépendantes des supports souples de la FC.

Le format FC fourni est interprété comme un entraxe de fixation de 30,5 × 30,5. La carte de 36 × 36 et ses composants restent indicatifs, faute de référence précise.

Les quatre ESC sont représentés par des cartes de 50 × 18 × 8, sur isolants de 2. La batterie au-dessus du châssis occupe 148 × 44 × 52, sur un pad de 7, avec deux sangles de largeur 20. Ces dimensions sont provisoires ; aucune référence, tension ou capacité n'est imposée.

Les quatre moteurs portent la référence demandée GTSkytenRC 3115 640KV. Leur modèle est simplifié : corps Ø38 × 33 et arbre M5. Aucun plan constructeur vérifié n'a été trouvé. Le perçage 19 × 19 M3, le dégagement central Ø9 et les dimensions extérieures doivent être mesurés sur les moteurs réels avant fabrication.

Le centre des moteurs est décalé de 7 sur chaque support pour dégager le perçage moteur des mortaises. Les hélices sont des tripales de diamètre 228,6 et de pas géométrique 127, avec deux sens de rotation de chaque. Leur profil est une représentation, pas une CAO constructeur.

## Découpe et contrôles

Les DXF contiennent les contours nominaux, sans compensation d'outil. La planche 600 × 600 contient les 18 pièces carbone et le coupon. Le plan 06 est un guide de perçage des cornières, pas un développé de tôle.

Le coupon reprend la forme des mortaises. De gauche à droite, leurs largeurs sont 4,000 / 4,025 / 4,050 / 4,075 / 4,100 / 4,150. Mesurer la plaque et tester le coupon avant la découpe finale. Le jeu de 0,05 n'est pas une tolérance d'usinage garantie.

Usiner uniquement le calque DECOUPE des pièces carbone. Bridage, ponts, passes et G-code restent à définir dans la FAO.

Le modèle est contrôlé sans interférence entre pièces carbone, fixations et équipements. Les disques des hélices sont espacés d'environ 32,2 et dégagent l'électronique et la batterie représentées. Ces contrôles concernent les volumes modélisés. La résistance, les vibrations et la tenue sous charge ne sont pas validées.

## Reconstruction

Exécuter construire.FCMacro dans FreeCAD, puis exporter_dxf.py avec Python et ezdxf. Garder sources/contours.json. Les fichiers intermédiaires sont générés dans .build/.

Les constantes d'épaisseur, de fraise et de jeu sont au début de la macro. Le tableau FreeCAD affiche ces valeurs mais ne recalcule pas les interfaces. Toute modification demande une reconstruction et un contrôle des emboîtements.
