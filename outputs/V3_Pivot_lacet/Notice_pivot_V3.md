# V3 — liaison entre socle et fourche

La V3 conserve la fourche, les cadres et le support du drone de la V2. La liaison de lacet est remplacée par une cartouche métallique sur arbre vertical, une butée axiale et un indexage sous disque.

## Modifications

- Deux paliers à bride **UCF204 pour arbre Ø20**, opposés, avec **64 mm entre centres de roulement**.
- Une **butée à billes 51104, 20 × 35 × 10**, porte le poids. Elle dispose de ses deux rondelles métalliques ; la couronne inférieure porte sur un pont métallique, la supérieure sous le moyeu tournant.
- Un **SHF20 métallique** relie l’arbre au plateau tournant. Son modèle CAO fabricant est inclus ; ses trous sont à ±23,75 mm, entraxe 47,5.
- Deux platines de cage et quatre tirants M10 définissent le montage des paliers. Leurs entraxes sont cotés dans le DXF.
- Une bague DIN 705 sous le palier inférieur ajoute une retenue de secours contre le soulèvement.
- Un disque CP non porteur à 24 trous et une vis d’indexage M6 accessibles par-dessous donnent un blocage tous les 15°. Le support imprimé porte l’effort d’indexage, pas le poids de la fourche.

La fourche est rehaussée de **130 mm**. Les axes du cardan sont maintenant à **895 mm**, hauteur neutre totale autour de 0,98 m. Les angles de la feuille FreeCAD restent B4/B5/B6.

## Chemins d’efforts

**Poids :** traverse 3060 → plateau AL05 → face large du SHF20 → rondelle tournante de la 51104 → butée → pont AL04 → entretoises métalliques → platine supérieure → tirants → platine inférieure → panneau CP05 → profilés du socle.

**Effort latéral et basculement :** plateau / moyeu → arbre Ø20 → deux inserts UCF204 espacés → cage métallique → socle.

**Blocage de lacet :** disque CP06 solidaire d’AL05 → vis M6 dans un trou du disque → écrou captif et bras imprimé → montant 3030 fixe et ses équerres → panneau du socle. Le disque ne porte pas verticalement la fourche.

Les deux vis de blocage de chaque insert UCF204 et la bague inférieure doivent être serrées selon les composants achetés. La bague est une retenue supplémentaire, pas une justification de résistance au soulèvement de tout le banc.

## Pièces plates à préparer

Les cotes complètes sont dans `Plans_pivot_V3.dxf`, en mm. Utiliser des plaques d’aluminium de qualité mécanique, par exemple 6082-T6, épaisseur 6. Ébavurer les deux faces, contrôler leur planéité et leur parallélisme au montage.

| Pièce | Format | Qté | Préparation |
|---|---|---:|---|
| CP05 | CP bouleau 600 × 400 × 18 | 1 | Ø55 central ; 8 Ø11 sur carrés 64 et 130 ; 4 Ø6,6 vers socle ; 2 Ø8,5 pour pied index |
| AL02 | Aluminium 160 × 160 × 6 | 1 | Ø55 central ; 8 Ø11 sur carrés 64 et 130 |
| AL03 | Aluminium 160 × 160 × 6 | 1 | AL02 + 4 Ø9 sur carré 100 |
| AL04 | Aluminium 120 × 120 × 6 | 1 | Ø21 central ; 4 Ø9 sur carré 100 ; coins coupés 6 × 6 pour dégager les contre-écrous |
| AL05 | Aluminium 160 × 240 × 6 | 1 | Ø21 ; 2 Ø6,6 entraxe 47,5 avec fraisures 90° ; 4 Ø6,6 vers traverse et 4 Ø5,5 vers disque |
| CP06 | Disque CP Ø400 × 18, trou Ø80 | 1 | 24 Ø6,5 sur Ø360 ; 4 Ø5,5 de fixation ; 4 accès Ø14 aux têtes des vis de traverse |

Les deux trous du pied indexeur se vérifient avec les équerres effectivement achetées avant perçage. Les autres perçages ne dépendent plus d’un plateau tournant d’ameublement à choisir. Les logements précis des roulements sont usinés dans les paliers achetés ; aucune portée de roulement n’est à tourner chez soi.

## Achats ajoutés pour le pivot

Conserver les composants du cardan de la V2. Retirer le roulement de plateau tournant, CP01/CP02 et les quatre M6x25 de liaison de CP02 à la traverse. Les quatre M6x25 de fixation de CP01 au socle sont réutilisées sur CP05.

| Achat | Qté | Remarque |
|---|---:|---|
| UCF204, palier carré Ø20, bride 86, entraxe 64 | 2 | Vérifier les dimensions avec la fiche de la référence achetée |
| Butée 51104, 20 × 35 × 10 | 1 | Livrée avec ses deux rondelles et cage à billes |
| Support SHF20 Motedis, entraxe 47,5 | 1 | Sert de moyeu tournant ; ne pas substituer une variante d’entraxe différent |
| Arbre acier lisse Ø20 × 200 | 1 | Sans filetage, extrémités ébavurées ; contrôler l’ajustement avec les inserts |
| Bague d’arrêt DIN 705, 20 × 32 × 14 | 1 | Vis pointeau fournie |
| Tige filetée M10, coupe 170 | 4 | Quatre coupes, pas de portée de roulement dans la tige filetée |
| Écrou M10 | 40 | 32 écrous / contre-écrous des tirants + 8 des paliers |
| Rondelle M10 | 32 | 16 aux tirants, 16 aux fixations des paliers |
| Vis hexagonale M10x50 | 4 | Palier inférieur, à travers panneau et platine |
| Vis hexagonale M10x35 | 4 | Palier supérieur sous sa platine |
| Entretoise métallique Ø8,5 traversant, longueur 12 | 4 | Appuis du pont de butée ; même longueur pour les quatre |
| M8x40 + écrou + deux rondelles | 4 jeux | Pont de butée sur platine supérieure |
| M6x30 fraisée 90° + écrou + rondelle | 2 jeux | SHF20 vers AL05, tête affleurante indispensable sous le profilé |
| M6x16 + rondelle + écrou B8 | 4 jeux | AL05 vers rainures inférieures de la traverse |
| M5x35 + écrou frein + deux rondelles | 4 jeux | Disque d’indexage vers AL05 |
| Profilé 3030 B8, longueur 120 | 1 | Montant fixe de l’indexeur |
| Équerre S8BBR30 + M6x12 / écrou B8 | 2 jeux | Partie verticale du pied ; fixation au bois par les M6x35 ci-dessous |
| M6x35 + écrou frein + deux rondelles | 2 jeux | Pied indexeur sur CP05 |
| M6x20 + rondelle + écrou B8 | 3 jeux | Fixation du capot imprimé au montant |
| Vis moletée ou à oreilles M6x35 | 1 | Pion d’indexage vissé, à manœuvrer par-dessous |
| Écrou M6 ordinaire, surplat 10 | 1 | Captif dans le bras imprimé ; ne pas utiliser un écrou frein dans cette poche |

Visserie acier de classe 8.8 pour les assemblages métalliques, sauf composant de manœuvre spécifié autrement par son fabricant. Les écrous, rondelles, graisseurs et vis de blocage intégrées aux paliers ne sont pas tous représentés dans la CAO. La boulonnerie réelle prime sur les enveloppes graphiques simplifiées.

## Montage de la cartouche

1. Monter CP05 sur les deux renforts existants du socle. Les huit passages Ø11 permettent les fixations des tirants et du palier bas ; le trou central dégage l’arbre et sa bague.
2. Poser AL02 à Z=63–69. Employer des rondelles larges sous le contreplaqué. Installer les tirants aux coins ±65 et le palier inférieur sur la face supérieure. Les M10x50 traversent aussi le CP. Prévoir les rondelles et écrous sous le panneau.
3. Monter AL03 à Z=163–169, avec le second palier sur sa face inférieure. Les faces de fixation des paliers sont donc à 69 et 163 ; leurs centres sont à 84 et 148. Régler les écrous pour garder les plaques parallèles. Les quatre tirants ont des contre-écrous de part et d’autre des plans maintenus.
4. Engager l’arbre, laisser d’abord les vis de blocage des inserts desserrées. Vérifier qu’il tourne librement et que l’auto-alignement des paliers n’est pas utilisé pour compenser une cage visiblement de travers.
5. Poser AL04 sur les quatre entretoises de 12. Les coins coupés dégagent les contre-écrous des tirants. Sa face supérieure est à Z=187. Vérifier le jeu sous AL04 au-dessus des têtes M10 du palier supérieur.
6. Monter les trois éléments de la butée 51104 dans le bon sens, selon la fiche fabricant. La rondelle fixe à alésage de dégagement repose sur AL04 ; la rondelle d’arbre tourne au-dessus. Lubrifier selon la prescription de la butée achetée. La butée ne remplace pas le guidage radial.
7. Orienter le SHF20 avec sa bride contre AL05 et son bossage vers le bas, au contact de la rondelle d’arbre. La face d’appui de bossage est nominalement Ø30 ; contrôler qu’elle porte correctement et sans bavure sur la rondelle. Les deux fraisures de fixation sont affleurantes : les têtes ne doivent pas pousser la traverse 3060.
8. Poser AL05 et la traverse. Les quatre vis M6 s’introduisent par-dessous AL05 ; les accès Ø14 du disque restent accessibles. Monter le disque comme accessoire sous AL05, avec les quatre M5 ; il entoure le moyeu sans lui toucher.
9. Asseoir le poids sur la butée, puis serrer les vis de blocage de l’arbre dans les inserts et le SHF20 conformément aux notices. Ne pas imposer de précharge axiale en tirant les paliers l’un contre l’autre. Régler la bague DIN 705 sous le palier bas avec environ 1 mm de jeu de secours, puis serrer sa vis.
10. Monter le montant fixe et le bras imprimé sous le disque. La face supérieure du bras est à Z=191, le dessous du disque à Z=199 : jeu nominal 8 mm. Le bras reste aussi sous la traverse, dont le dessous est à Z=223, quelle que soit sa direction.

Vérifier les dimensions réelles du SHF20, des paliers et de la butée avant de percer l’interface définitive. Les modèles des UCF204 et de la butée sont des enveloppes dimensionnelles, pas leurs géométries internes détaillées. L’auto-alignement ne dispense pas de la mise en ligne.

## Indexage manuel

Le pion est une vis à poignée M6x35 traversant un écrou captif du bras. Elle est manœuvrée depuis le dessous. En retrait, son extrémité reste sous le disque ; engagée dans un trou, elle en bloque la rotation à l’un des 24 angles. Il n’y a pas d’écrou papillon au-dessus du disque, pour préserver le passage de la traverse.

Retirer suffisamment la vis avant de tourner, sans sortir complètement la vis de l’écrou captif. Soutenir le montage, aligner le trou, engager sans forcer. La vis ne doit pas se transformer en vérin poussant le disque : son rôle est de servir de pion. Une lecture des angles imprimés ne garantit pas une précision métrologique ; vérifier la position au niveau / inclinomètre pour la calibration.

## Impression

Tous les STL de la V2 sont conservés. Ajouter **10_Bras_index_lacet_x1.stl**, enveloppe 110 × 50 × 48, compatible 220 × 220. PETG, 6 périmètres, remplissage 50–60 %, supports sous la toiture et le bras en porte-à-faux. Reprendre les passages M6 sans agrandir les logements d’écrou. Cette pièce ne supporte pas le poids vertical du banc.

Le dossier contient 12 formes STL : 25 pièces du banc, plus le coupon et le gabarit, soit 27 impressions si tout est reconstruit. Les chapitres de montage des parties hautes V2 restent applicables ; la présente notice remplace entièrement leur ancien montage de lacet.

## Cas de calcul et vérifications

Le drone reste donné pour 2 kg. La masse tournante est supérieure à 2 kg puisqu’elle comprend profilés, cadres, arbres, accessoires et plateau. Un cas préliminaire de **400 N verticaux et 20 N·m de basculement** sert à contrôler l’ordre de grandeur du pivot ; il ne définit pas une charge admissible du banc.

Pour un écartement de guidage de 64 mm, le couple de 20 N·m produit une paire radiale d’environ **313 N**. La contrainte de flexion idéale d’un arbre plein Ø20 sous ce moment vaut environ **25,5 MPa**, avant effets locaux des serrages et contacts. La validation de la cage, des panneaux, des vis de blocage, de la rigidité et du montage complet reste à effectuer sur prototype. Les capacités catalogues des roulements ne sont pas celles du banc assemblé.

Les vérifications CAO sont consignées dans les JSON : validité des solides et maillages, encombrement d’impression, positions de lacet échantillonnées et dégagement des écrous de la cage. Elles n’incluent pas les déformations, le frottement réel, la qualité du CP ou de l’impression, ni la tenue sous charge. Essayer d’abord la liaison seule, puis la structure avec une masse inerte retenue, avant le drone. Usage prévu : manipulation manuelle statique, sans hélices.

## Sources dimensionnelles

- [SNR UCF204 : bride 86, entraxe 64, hauteur 33,3, centres et insert](https://eshop.ntn-snr.com/pt/product/UCF204-SNR/UCF204).
- [NSK 51104 : dimensions 20 × 35 × 10 et appuis](https://www.nsk.com/jp-ja/engineering/51104-tb-sd.html).
- [Motedis SHF20 : modèle fabricant et fixation sans usinage des extrémités d’arbre](https://www.motedis.fr/fr/Supports-darbre-SHF20).

Le STEP SHF20 et la CAO des profilés / équerres sont fournis dans Sources. `Revoir_pivot_V3.FCMacro` ouvre la copie V2 incluse puis reconstruit uniquement cette liaison ; garder l’arborescence. Le fichier FCStd livré contient directement la V3 complète.
