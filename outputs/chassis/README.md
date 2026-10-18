# Châssis CNC

Carbone de 4 mm. Fraise Ø3 mm. Révision R6. Dimensions en mm.

[FreeCAD](chassis.FCStd) | [STEP](chassis.step) | [DXF](dxf/) | [Composants](composants.csv)

[Prototype MDF 4 mm : fichiers pour découpe laser](laser/README.md)

## Liaisons

Les bras sont pleins, sans trou d’allègement ni perçage transversal. Les encoches sur les transitions libres sont supprimées et remplacées par des raccords tangents de rayon 8. Les dégagements de fraise restent limités aux épaulements des tenons.

Les tenons mesurent 14 de long aux racines et 12 côté moteur. Les mortaises font respectivement 14,08 × 4,05 et 12,08 × 4,05, avec des dégagements de fraise localisés aux coins. Le jeu nominal total en épaisseur est de 0,05.

Les équerres et leurs vis transversales sont supprimées. Les tenons positionnent les bras entre les platines. Deux entretoises métalliques de 20 et deux vis M3 par racine ferment les platines centrales. Cinq entretoises de 16 et cinq vis M3 ferment chaque paire de socles moteurs, dont deux fixations supplémentaires près de l’arrivée des bras.

Les socles moteurs ont un contour effilé avec des raccords de rayon 8 de 57,9 × 58, avec les mêmes axes moteurs et mortaises. La distance minimale entre un perçage ou une mortaise et le bord est de 3,77.

Espacement intérieur des platines centrales : 20. Espacement intérieur des supports moteurs : 16. Entretoises et visserie détaillées dans le CSV. Les vis et écrous sont simplifiés dans la CAO ; les rondelles sont comptées dans le CSV.

Les platines centrales mesurent 120 × 250, avec un contour arrondi et les seuls perçages de fixation utilisés. Les sangles de batterie, axes moteurs, entraxes et bras restent identiques à la révision R5. Le volume des pièces carbone diminue de 4,8 %.

## Pièces carbone

| Pièce | Quantité | Dimensions |
|---|---:|---|
| Platine centrale | 2 | 120 × 250 × 4 |
| Bras court | 4 | 160 × 28 × 4 |
| Bras long | 4 | 190 × 28 × 4 |
| Socle moteur | 8 | 57,9 × 58 × 4 |
| Coupon d'ajustement | 1 | 84 × 32 × 4 |

## Équipements

La FC et les quatre ESC sont placés entre les platines. Les fixations structurelles centrales sont indépendantes des supports souples de la FC.

Le format FC fourni est interprété comme un entraxe de fixation de 30,5 × 30,5. La carte de 36 × 36 et ses composants restent indicatifs, faute de référence précise.

Les quatre ESC sont représentés par des cartes de 50 × 18 × 8, sur isolants de 2, maintenus par quatre colliers nylon 2,5 × 100. Six fenêtres de 8 × 4 permettent le passage des colliers ; la fenêtre centrale de chaque rangée est partagée. La batterie au-dessus du châssis occupe 148 × 44 × 52, sur un pad de 7, avec deux sangles de largeur 20. Ces dimensions sont provisoires ; aucune référence, tension ou capacité n'est imposée.

Les quatre moteurs portent la référence demandée GTSkytenRC 3115 640KV. Leur modèle est simplifié : corps Ø38 × 33 et arbre M5. Aucun plan constructeur vérifié n'a été trouvé. Le perçage 19 × 19 M3, le dégagement central Ø9 et les dimensions extérieures doivent être mesurés sur les moteurs réels avant fabrication.

Le centre des moteurs est décalé de 7 sur chaque support pour dégager le perçage moteur des mortaises. Les hélices sont des tripales de diamètre 228,6 et de pas géométrique 127, avec deux sens de rotation de chaque. Leur profil est une représentation, pas une CAO constructeur.

## Découpe et contrôles

Les DXF contiennent les contours nominaux, sans compensation d'outil. La planche 600 × 600 contient les 18 pièces carbone et le coupon.

Le coupon reprend la forme des mortaises. De gauche à droite, leurs largeurs sont 4,000 / 4,025 / 4,050 / 4,075 / 4,100 / 4,150. Mesurer la plaque et tester le coupon avant la découpe finale. Le jeu de 0,05 n'est pas une tolérance d'usinage garantie.

Usiner uniquement le calque DECOUPE des pièces carbone. Bridage, ponts, passes et G-code restent à définir dans la FAO.

Le modèle est contrôlé sans interférence entre pièces carbone, fixations et équipements. Les disques des hélices sont espacés d'environ 32,2 et dégagent l'électronique et la batterie représentées. Ces contrôles concernent les volumes modélisés. La résistance, les vibrations et la tenue sous charge ne sont pas validées.

## Reconstruction

Exécuter construire.FCMacro dans FreeCAD, puis exporter_dxf.py avec Python et ezdxf. Garder sources/contours.json. Les fichiers intermédiaires sont générés dans .build/.

Les constantes d'épaisseur, de fraise et de jeu sont au début de la macro. Le tableau FreeCAD affiche ces valeurs mais ne recalcule pas les interfaces. Toute modification demande une reconstruction et un contrôle des emboîtements.
