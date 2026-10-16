# Châssis CNC

Carbone de 4 mm. Fraise Ø3 mm. Dimensions en mm.

[FreeCAD](chassis.FCStd) | [STEP](chassis.step) | [DXF](dxf/) | [Composants](composants.csv)

| Pièce | Quantité | Dimensions |
|---|---:|---|
| Platine centrale | 2 | 128 × 270 × 4 |
| Bras court | 4 | 160 × 28 × 4 |
| Bras long | 4 | 190 × 28 × 4 |
| Socle moteur | 8 | 50,32 × 64,32 × 4 |
| Coupon d'ajustement | 1 | 84 × 32 × 4 |

Rainures de 4,2 de large. Longueur 17,6 dans les platines centrales et 15,6 dans les socles moteurs. Rayons rentrants des épaules des bras : 1,6. Trous de fixation M3 : Ø3,3.

Les centres de fixation du LithFrame sont conservés. Les petits décors et les trous Ø2,2 du motif électronique ont été supprimés.

## Découpe

Les DXF contiennent les contours nominaux, sans compensation d'outil. La planche 600 × 600 contient les 18 pièces et le coupon, avec au moins 10,679 entre pièces.

Usiner le calque DECOUPE. Les calques ANNOTATIONS_NE_PAS_USINER et PLAQUE_REFERENCE sont des repères. Le bridage, les ponts, les passes et le G-code restent à définir dans la FAO.

Le coupon propose, de gauche à droite, des rainures de 4,00 / 4,10 / 4,20 / 4,30 / 4,40 / 4,50. Tester l'ajustement avec la plaque réelle avant de découper les autres pièces.

## Vérifications

Aucune interférence détectée entre les 18 pièces carbone assemblées. Les cinq DXF individuels ont été réimportés et comparés aux profils FreeCAD. Le STEP assemblé contient 34 solides valides, entretoises comprises.

Les contours cumulés mesurent 11,99 m contre 13,81 m pour les profils d'origine. À épaisseur égale, le volume de carbone augmente de 13,8 %. Ces chiffres ne donnent ni le temps machine ni la résistance.

Le dégagement moteur Ø12 laisse localement 1,85 de matière jusqu'aux trous de fixation. Vérifier cette zone et la compatibilité avec les moteurs réels. Aucun calcul structurel ni essai sous charge n'a été réalisé.

## Reconstruction

Exécuter construire.FCMacro dans FreeCAD, puis exporter_dxf.py avec Python et ezdxf. Garder sources/contours.json. Les fichiers intermédiaires sont générés dans .build/.

Les constantes d'épaisseur, de fraise et de jeu sont au début de la macro. Le tableau FreeCAD affiche ces valeurs mais ne recalcule pas les interfaces. Toute modification demande une reconstruction et un nouveau contrôle des emboîtements.
