# Banc IMU / test multiaxe — LithFrame F380 à enveloppe 500 mm

Version du 16 octobre 2026 — avant-projet CAO manuel.

## Livrables

- `Banc_IMU_F380_500.FCStd` : assemblage FreeCAD natif, pièces regroupées par axe.
- `Banc_IMU_F380_500.step` : échange 3D, position neutre.
- `Ebauches_anneaux_platine.dxf` : contours 2D des anneaux et de la platine, en mm. Ce sont des ébauches ; les perçages des chapes ne sont pas encore définis.
- `Construire_banc_IMU.FCMacro` et `contours_source.json` : construction reproductible à l’emplacement de ce dossier.
- Images d’ensemble et inclinée ; rapports JSON des contrôles.

## Architecture retenue

Trois rotations imbriquées : lacet Z, tangage Y, roulis X. La fourche tourne sur un pivot vertical. L’anneau extérieur bascule autour de deux tourillons Y ; l’anneau intérieur bascule autour de deux tourillons X. Le support de drone reste solidaire de l’anneau intérieur.

| Élément | Géométrie nominale |
|---|---|
| Cadre de base | 1 000 × 1 000 mm hors patins ; environ 1 020 mm avec patins |
| Centre des axes | Z = 650 mm au-dessus du dessous des patins |
| Hauteur en position neutre | 715 mm environ, index inclus |
| Anneau de tangage | Ø730 extérieur / Ø682 intérieur / épaisseur 16 mm |
| Anneau de roulis | Ø620 extérieur / Ø572 intérieur / épaisseur 16 mm |
| Montants de fourche | Entraxe 850 mm ; section 60 × 40 mm modélisée pleine |
| Traverse de fourche | 60 × 900 × 60 mm, modélisée pleine |
| Axes de tangage et roulis | Ø20 mm |
| Paliers de tangage / roulis | Enveloppes de roulements 6004, 20 × 42 × 12 mm ; 4 roulements au total |
| Platine d’adaptation | 160 × 300 × 8 mm |
| Indexation | Disques à 24 trous ; pas géométrique de 15° |
| Drone cible | Cylindre enveloppe Ø500 × 160 mm centré sur les axes ; hélices déposées |

Le cylindre cible est masqué dans le groupe de référence du drone. Il représente une limite d’encombrement choisie, pas une mesure de votre drone complet. La diagonale désigne ici l’encombrement extérieur total sans hélices, et non uniquement l’entraxe des moteurs.

Les anneaux et les montants pleins sont des choix de géométrie initiale. Ils peuvent être allégés après calcul et définition des assemblages. Aucun poids maximal admissible n’est attribué à cette version.

## Exploitation des DXF fournis

Les fichiers originaux restent inchangés. Les unités des pièces individuelles sont en mm. Dimensions mesurées : base 126 × 270 mm, bras court 160 × 28 mm, bras long 190 × 28 mm. La base comporte des carrés de perçages de 50 et 70 mm, trous Ø4,5 mm, repris sur la platine proposée. Quatre lumières de largeur 6,5 mm et longueur totale 30,5 mm permettent des reprises de fixation.

Les contours LINE / ARC / CIRCLE ont été reconstruits en faces puis extrudés. Quelques raccords de la base comportaient de petits écarts : une tolérance de connexion de 0,01 mm a permis de fermer les contours. Les entités 3DSOLID du DXF n’ont pas servi à déduire l’épaisseur : 3 mm est une hypothèse explicite pour la référence carbone, à confirmer.

La base exacte est visible dans le support. Les quatre pièces sources extrudées sont disponibles dans le groupe masqué « Pièces DXF sources ». Les positions d’assemblage des bras ne sont pas déductibles de façon certaine des pièces à plat ; aucun drone complet fictif n’a été assemblé.

Les entretoises de référence sont sur le carré de 50 mm. Confirmer qu’il est disponible sur le drone réel, sans conflit avec l’électronique, puis prévoir le serrage et le maintien des entretoises sur la platine.

## Modifier les positions dans FreeCAD

Ouvrir le fichier FCStd puis la feuille « Paramètres ». Modifier seulement les cellules suivantes pour piloter l’ensemble :

- B10 : lacet en degrés ;
- B11 : tangage en degrés ;
- B12 : roulis en degrés.

Les autres valeurs décrivent la géométrie nominale. Certaines dimensions de primitives sont liées à la feuille, mais les paliers, les chapes et tous les accessoires ne suivent pas automatiquement : un changement de dimensions exige une reprise cohérente des pièces et des contrôles. Cette version n’est donc pas un configurateur dimensionnel complet.

| Direction du Z de la platine dans le repère fixe | Lacet | Tangage | Roulis |
|---|---:|---:|---:|
| +Z | 0° | 0° | 0° |
| −Z | 0° | 180° | 0° |
| +X | 0° | 90° | 0° |
| −X | 0° | −90° | 0° |
| +Y | 0° | 0° | −90° |
| −Y | 0° | 0° | 90° |

Ces signes décrivent le repère CAO ; les axes du contrôleur de vol doivent être identifiés séparément. À tangage ±90°, le montage présente la singularité habituelle d’un cardan : cela n’empêche pas une pose statique, mais supprime l’indépendance instantanée de deux axes. Les câbles et les pions d’indexage limitent la rotation réelle ; aucune rotation continue sous câblage n’est revendiquée.

## Contrôles réalisés

- 68 solides mécaniques visibles : BRep valides et volumes positifs.
- Six orientations cardinales et une orientation combinée 35° / 40° / 25° : aucun recouvrement volumique détecté entre les pièces contrôlées du porte-drone et la traverse / les montants de fourche.
- Huit positions de tangage / roulis : aucun recouvrement entre les pièces contrôlées du groupe intérieur et l’anneau extérieur, hors chapes et tourillons, dont les interfaces sont intentionnelles.
- Dégagement radial théorique du cylindre drone vers l’intérieur de l’anneau : 286 − √(250² + 80²) ≈ 23,5 mm.
- Écart théorique de l’anneau intérieur seul vers l’anneau extérieur : environ 30,9 mm.
- Export STEP produit ; images obtenues depuis la vue FreeCAD réelle.

Les contrôles sont ciblés et discrets : ils ne prouvent pas l’absence de toute collision sur une trajectoire continue et n’incluent pas le vrai drone assemblé, le câblage, les mains de l’opérateur ou les pions rétractés. Ils ne constituent ni une étude de résistance, ni une preuve de rigidité ou de précision métrologique.

## Fonction couverte et suite mécanique

Cette base sert à définir un positionneur manuel pour les poses statiques d’accéléromètre et les vérifications de signes d’attitude. Une vitesse imposée et mesurée est nécessaire pour vérifier quantitativement le facteur d’échelle d’un gyroscope ; elle n’est pas fournie par une manœuvre manuelle ou par les angles de la CAO.

La calibration d’accéléromètre en six positions est documentée par [ArduPilot](https://ardupilot.org/copter/docs/common-accelerometer-calibration.html). Suivre la procédure propre au contrôleur installé et attendre l’immobilité après chaque mouvement. Le support ne dispense pas du réglage de niveau de référence.

Avant fabrication :

1. Relever la masse, le centre de gravité, l’encombrement réel complet et la position de l’IMU. Adapter la hauteur du support pour approcher l’IMU et le centre de gravité du centre des axes ; les 43 mm d’entretoise actuels sont indicatifs.
2. Dimensionner rigidité, flèche, axes, roulements, basculement du socle et ancrages pour la charge réelle et les efforts de manipulation. Les tubes du socle sont modélisés en 40 × 40 × 3 mm, sans assemblages définitifs.
3. Définir les fixations des chapes sur les anneaux, les fixations des paliers et des colonnes, la liaison de la platine aux rails, les assemblages du socle, les moyeux de disques, les épaulements et la retenue axiale des axes. Plusieurs interfaces de la maquette sont représentées en contact ou avec recouvrement, sans visserie complète.
4. Définir les ajustements des logements Ø42 et axes Ø20, la retenue des bagues et le jeu axial. Les dimensions nominales 6004 sont cohérentes avec le [catalogue SKF](https://cdn.skfmediahub.skf.com/api/public/094cc500316fc14e/pdf_preview_medium/094cc500316fc14e_pdf_preview_medium.pdf) ; la sélection définitive dépendra des charges.
5. Détailler des indexeurs rétractables captifs, leurs ressorts, leur maintien et des freins séparés. Les pions et poignées visibles sont des volumes fonctionnels ; ils ne représentent pas un mécanisme de frein fini. Prévoir le déséquilibre en cas de libération d’un axe.
6. Définir le cheminement des câbles, les butées et la protection contre le pincement. Prévoir des repères gravés et vérifier l’équerrage des trois axes avec un moyen externe.

Pour le magnétomètre, la structure et les roulements peuvent perturber le champ : une validation séparée est nécessaire. Voir les [recommandations ArduPilot sur le compas](https://ardupilot.org/copter/docs/common-compass-setup-advanced.html).

Les essais moteurs et la stabilisation avec hélices sortent du domaine de cette V1. Ils exigent une étude des efforts, des vibrations, des protections et de la dynamique du banc. Une évolution de calibration gyroscopique demanderait des entraînements, des codeurs, une commande de vitesse, une référence temporelle et une validation métrologique.

## Support de pilotage FreeCAD

L’extension [FreeCAD MCP de neka-nat](https://github.com/neka-nat/freecad-mcp) a été copiée dans le dossier utilisateur Mod de FreeCAD 1.1. Son pont RPC local a été lancé sur 127.0.0.1:9875 et testé par ping et exécution de code : il a servi à compléter et vérifier le modèle.

Le serveur MCP externe est installé dans un environnement Python dédié. Le fichier `freecad_mcp_client.json` fournit une entrée de configuration du client ; il ne remplace pas la configuration existante de Codex et n’a pas été fusionné automatiquement avec elle. Aucun outil MCP FreeCAD n’a été enregistré à chaud dans cette conversation : le pilotage effectué ici utilise le pont RPC de l’extension.

Pour une session suivante, sélectionner l’atelier « MCP Addon » puis démarrer « Start RPC Server ». Garder le serveur limité à la machine locale. Voir `etat_mcp.txt` pour le chemin effectivement utilisé. L’installation utilise deux composants distincts, comme indiqué dans la [documentation du projet](https://github.com/neka-nat/freecad-mcp/blob/main/docs/installation.md).

