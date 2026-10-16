# Banc IMU V2 — construction amateur / drone de 2 kg

Cette V2 remplace les anneaux de la première proposition par deux cadres en profilés. Elle conserve les trois rotations manuelles et la fixation de référence du LithFrame. Les fichiers de la V1 restent séparés.

## Ce qui est prêt

- Assemblage FreeCAD, STEP et macro de reconstruction.
- 21 profilés à couper droit, sans taraudage ni perçage des profilés.
- Deux plaques de liaison plates en aluminium, des panneaux de contreplaqué et de la quincaillerie standard.
- 11 modèles STL : 24 pièces du banc, un coupon d’ajustement et un gabarit de pointage. Chaque pièce tient séparément sur 220 × 220 mm.
- Liste de coupes, achats et visserie ; DXF des pièces plates et de leurs perçages connus.

La donnée de conception est un drone complet de **2 kg**, sans hélices, dans l’enveloppe cible Ø500 × 160 mm. Le modèle ne constitue pas une charge admissible certifiée : le premier assemblage imprimé doit être essayé progressivement avant d’y confier le drone. Le choix du roulement de lacet et le report de ses perçages sur les deux panneaux restent à faire selon la pièce effectivement achetée.

## Architecture et repères

Le socle mesure 1 000 × 1 000 mm. Une couronne de plateau tournant est prise entre deux panneaux CP de 400 × 400 × 18. Une traverse 3060 de 950 mm porte deux montants de 600 mm, placés à Y = ±460 mm. Les axes de tangage sont à Z = 765 mm, au-dessus du bout des montants : les arbres passent librement sans traverser leur métal.

Le cadre de tangage fait 720 × 720 mm ; ses côtés suivant Y sont interrompus sur 100 mm au milieu. Deux plats AL01 de 80 × 200 × 3 relient solidement les quatre segments de 280 mm et portent les paliers de roulis. Leur trou Ø38 libère le passage de l’arbre et de sa bague d’arrêt. Cette construction évite d’usiner un gros trou transversal dans le profilé.

Le cadre de roulis fait 620 × 620 mm. Quatre consoles imprimées portent deux rails 3030 de 544 mm, puis un panneau CP de 180 × 300 × 12. Le carbone repose sur quatre entretoises métalliques M4 de 20 mm. Les perçages à carrés de 50 et 70 mm correspondent aux contours de la base DXF fournie.

La hauteur neutre est d’environ 0,85 m. Prévoir de l’espace au-dessus pour l’inclinaison, environ 1,35 m depuis le sol, ainsi que le passage des mains. La masse des seuls profilés est estimée autour de 13 kg à partir des sections fabricant et de la densité usuelle de l’aluminium ; la structure est volontairement robuste plutôt qu’allégée. Les paliers portent aussi les cadres et accessoires, en plus du drone.

X = direction des axes de roulis, Y = direction des axes de tangage, Z = verticale en position neutre. La succession des rotations est lacet Z, tangage Y, roulis X. À tangage ±90°, le cardan a sa singularité cinématique habituelle ; une pose statique reste possible.

## Outils et préparation

Prévoir une scie à métaux ou une commande de profilés coupés, une scie sauteuse pour le CP, une perceuse, un étau ou des serre-joints, une scie-cloche métal Ø38, des forets adaptés aux trous Ø4,5 et Ø6,6, une équerre, un pied à coulisse et des clés Allen. Ébavurer les coupes et les axes. Les deux petites tôles AL01 se percent bridées, avec un martyr ; ne pas tenir une plaque libre à la main.

Les profilés, équerres et écrous doivent tous être **Type B rainure 8**. Un profilé 3030 Type I rainure 6 n’est pas interchangeable. Les STEP du fournisseur sont inclus dans Sources et ont servi aux sections réelles du modèle.

Lire `Liste_coupes_et_achats.md` avant de commander. Le fichier `Plans_percage_bois_et_ponts.dxf` est en mm, à l’échelle 1:1. Si impression papier, désactiver l’ajustement à la page et contrôler une distance connue au réglet.

## Impression sur 220 × 220 mm

Matériau de départ : PETG correctement séché. Prusa décrit son usage pour des [pièces mécaniques, supports et colliers](https://help.prusa3d.com/article/petg_2059). Les réglages ci-dessous sont un point de départ d’atelier, pas des valeurs de résistance garanties.

- Buse 0,4 mm, couches 0,20 mm ; 6 périmètres, 6 couches pleines dessus / dessous ; 45 à 60 % de remplissage sur les pièces structurelles.
- Pas de mise à l’échelle globale des STL : les entraxes de vis doivent rester exacts. Si besoin, modifier les diamètres de logement dans la macro après essai du coupon.
- Les STL sont déjà orientés. Le palier de tangage a sa semelle sur le plateau ; un support local sous le petit épaulement intérieur peut être utile. Le palier pont a ses deux semelles sur le plateau.
- Les consoles 05 sont couchées sur le côté, pour orienter leurs couches dans le plan de leur forme en L. Reprendre les trous au foret plutôt que forcer les vis.
- Les bras 07 se posent sur leur semelle ; activer des supports sous la potence supérieure. Les couvercles, moyeux, volants, entretoises et gabarits ont une face plane sur le plateau.
- Sur les pièces de 200 mm, limiter la bordure à environ 5 mm pour rester dans le plateau de 220 mm.

Imprimer d’abord **00_Coupon_ajustement_x1**. À plat, X croissant de gauche à droite : grands trous de la rangée Y=30 : Ø41,9 / 42,0 / 42,1 / 42,2 ; petits trous de la rangée Y=78 : Ø20,0 / 20,1 / 20,2 / 20,3. Le modèle utilise un logement de roulement Ø42,2 et des moyeux Ø20,2 avant serrage. Le roulement doit entrer à la main avec un ajustement maîtrisé ; pas de marteau ni de contrainte imposée par un alésage trop petit.

Pour modifier les logements : dans la macro, la valeur 21,1 est le rayon de poche de roulement ; 10,1 est celui des moyeux et volants. Conserver les entraxes. Les cages ne doivent pas être ovalisées par le serrage.

Les noms x2 / x4 donnent le nombre d’exemplaires à lancer. Le ZIP des STL contient une seule géométrie par forme.

## Assemblage, dans l’ordre

### 1. Socle

Assembler les deux longueurs de 1 000 et les deux côtés de 940 pour obtenir 1 000 hors tout. Installer les deux renforts de 940 parallèles à Y, axes X = ±100. Utiliser 12 équerres avec leurs kits : 4 angles de cadre et deux équerres à chaque extrémité des deux renforts. Mettre les patins, régler les diagonales et serrer.

Fixer CP01 sur les renforts avec quatre M6x25, rondelles et écrous B8. Le socle doit reposer sans balancement et être immobilisé sur le plan de travail avant les manipulations.

### 2. Plateau de lacet : adaptation à la pièce achetée

Choisir un roulement de plateau tournant **captif, boulonnable aux deux faces**, d’environ Ø300, épaisseur 12 mm pour l’empilement fourni. Le dimensionner pour la masse totale de la fourche, des cadres et du drone, ainsi que le moment de renversement ; la seule masse du drone ne suffit pas. Éviter les simples plateaux de présentation posés sans fixation axiale.

Reporter les perçages du fabricant sur CP01 et CP02. Prévoir les accès aux vis selon sa méthode de montage. Les quatre trous déjà dessinés sur chaque panneau sont ceux des profilés, pas ceux du roulement. Fixer les deux bagues à leurs panneaux sans relier accidentellement les bagues entre elles.

Le modèle représente une enveloppe du roulement, pas un mécanisme de précision détaillé. Si son épaisseur diffère de 12 mm, corriger l’empilement avant montage : la traverse doit être horizontale et les deux axes de tangage doivent rester coaxiaux. Pour un diamètre voisin, vérifier l’absence de conflit avec les trous des panneaux.

Fixer la traverse 3060 sur CP02 depuis le dessous avec quatre M6x25, aux coordonnées X=±15 et Y=±170. Ces trous sont hors de l’enveloppe du roulement Ø300. Les deux serre-joints permettent ensuite de maintenir le lacet en pose ; les placer de part et d’autre de la traverse sur une zone commune aux deux panneaux et les retirer avant toute rotation.

### 3. Fourche

Positionner les deux montants 3060 à Y=±460, avec la largeur 60 suivant X. Ils reposent sur la traverse, Z=123 à 723. Deux équerres sont placées côté intérieur de chaque pied. Fixer ensuite les quatre goussets CP03 sur les faces latérales, par trois M6x25 chacun, dans les rainures latérales des montants et de la traverse.

Les trois trous du gousset sont à 20 mm au moins des bords droits. Le DXF donne le triangle de 250 × 250 et ses perçages ; ne pas réutiliser la petite forme de la V1.

Les centres des paliers de tangage sont 42 mm au-dessus du haut des montants, à Z=765. Leurs deux vis de semelle sont 55 mm sous l’axe, dans les deux rainures de la face intérieure du 3060. La semelle basse porte sur cette face ; le bloc du roulement reste au-dessus du montant.

### 4. Fabriquer les quatre paliers

Pour chaque corps 01 ou 01B, charger par la grande face ouverte : un 6004, l’entretoise imprimée 09 de 13,8, puis le second 6004. L’entretoise touche uniquement les **bagues extérieures**. Le premier roulement s’arrête sur l’épaulement intégré. Fermer avec un couvercle 02 ou 03.

Il n’y a qu’un couvercle ajouté par palier : deux simples et deux d’indexage au total. Les roulements doivent rester coaxiaux et tourner librement sur l’arbre avant serrage final. Les quatre vis M4 sont traversantes, avec rondelles et écrous frein métalliques. Sur chaque palier avec bras 07, deux vis M4x65 remplacent deux M4x55 et traversent aussi la semelle du bras.

Le couvercle 03 et le bras 07 vont sur le côté positif de tangage et le côté positif de roulis. La potence doit se trouver à l’extérieur du disque, sans le toucher. Les volants ont des trous tous les 15° : la lecture visuelle et les trous imprimés ne remplacent pas un contrôle d’angle.

### 5. Cadre de tangage et plaques ponts

Assembler les deux traverses de 720 et les quatre segments de 280. Hors tout 720 ; chaque côté suivant Y comporte une ouverture centrale de 100, de Y=-50 à +50. Réaliser les deux plats AL01 80 × 200 × 3 : trou Ø38 central et quatre trous Ø6,6 sur la ligne centrale à Y=±65 et ±85. Utiliser le gabarit 08 pour pointer.

Les plats se fixent aux faces **extérieures** des côtés interrompus. Le corps de palier pont 01B porte sur le plat et ses quatre M6x20 passent aussi à travers le plat avant d’atteindre les écrous dans les quatre rainures des segments. Les premiers écrous sont donc à 15 mm de l’extrémité des segments, pas à cheval sur la coupe.

Le plat métallique assure la continuité du cadre ; ne pas l’omettre. Cette disposition conserve les profilés intacts et laisse passer les bagues d’arrêt au centre.

Installer les deux moyeux 04 sur les faces extérieures des traverses Y=±360 du cadre de tangage. Leurs deux M6x16 se fixent à la rainure, sans percer le profilé. Enfoncer les arbres dans la partie fendue des moyeux ; leur extrémité s’arrête au-dessus de la semelle de 8 mm. Insérer les écrous M5 dans les logements hexagonaux et serrer progressivement les deux M5x60 de chaque moyeu.

Présenter le cadre dans la fourche, engager les arbres dans les paliers, aligner et serrer les fixations de paliers seulement après avoir vérifié la rotation libre.

### 6. Cadre de roulis et retenue axiale

Assembler un cadre de 620 hors tout avec deux traverses de 620 et deux côtés de 560. Les moyeux vont sur les faces X=±310. Les arbres traversent l’ouverture centrale des plats AL01, puis les paliers 01B, sans traverser le métal des profilés.

Installer **deux bagues DIN 705 par arbre**. Elles doivent serrer sur l’arbre ; leur diamètre extérieur 32 passe dans les ouvertures des paliers. Utiliser les rondelles fines pour que l’appui axial porte exclusivement sur les bagues intérieures des roulements. Empiler trois rondelles de 1 mm du côté de l’épaulement intégré et une de 1 mm côté couvercle, selon la CAO. Vérifier sur les roulements achetés qu’aucune rondelle ne frotte un joint ou une bague extérieure ; adapter l’épaisseur et le diamètre d’appui si nécessaire.

Régler un très faible jeu axial, sans précharge : les deux paliers opposés ne doivent pas se tirer l’un l’autre. Les positions CAO des bagues sont nominales ; le réglage se fait sur la construction réelle. Les vis pointeau des bagues DIN 705 doivent être accessibles et serrées. Un petit méplat local sur un arbre non trempé peut améliorer leur assise ; ne pas utiliser une tige filetée à la place d’un arbre.

Monter les deux volants avec leurs écrous et M5x60. Celui du tangage est déporté au-delà du montant pour que le disque ne puisse pas heurter son sommet. Ne pas compter sur le volant imprimé comme unique retenue axiale : les bagues métalliques sont indispensables.

### 7. Support du drone

Fixer les quatre consoles 05, deux sur chaque côté du cadre intérieur, aux positions Y=±90. Deux M6x16 fixent chaque console sur la rainure supérieure du cadre. Les consoles portent les deux rails de 544 ; une M6x16 sous chaque console atteint un écrou dans la rainure inférieure du rail.

Poser CP04 sur les rails et le fixer par quatre M6x20. Les carrés de 50 et 70 permettent l’adaptation au carbone fourni. La référence visible utilise le carré de 50 avec quatre entretoises métalliques de 20 et des M4x45 traversantes. Contrôler la disponibilité de ces trous sur le drone réel et les dégagements de l’électronique avant de monter.

Régler la position du drone, la hauteur des entretoises et, si nécessaire, la position de CP04 pour approcher son centre de gravité du croisement des axes. La hauteur de 20 mm est une hypothèse, pas une mesure du drone. Ajouter un maintien secondaire indépendant adapté au châssis, qui reste hors des trajectoires.

### 8. Indexage et utilisation

Soutenir la charge à la main, retirer les deux goupilles M5 et leurs écrous papillon, puis orienter doucement. À la position choisie, aligner le trou de la potence et l’un des 24 trous du volant, insérer la M5x35 et la retenir avec l’écrou papillon. Les goupilles sont représentées retirées dans la CAO pour permettre la visualisation des rotations.

Les deux goupilles maintiennent tangage et roulis ; les serre-joints maintiennent le lacet. Ne pas libérer un axe chargé et déséquilibré sans le soutenir. Les passages de câbles doivent être vérifiés avant chaque nouvelle amplitude.

Pour les six poses statiques, dans la feuille Paramètres du FCStd :

| Z de la platine dirigé vers | Lacet B4 | Tangage B5 | Roulis B6 |
|---|---:|---:|---:|
| +Z | 0° | 0° | 0° |
| −Z | 0° | 180° | 0° |
| +X | 0° | 90° | 0° |
| −X | 0° | −90° | 0° |
| +Y | 0° | 0° | −90° |
| −Y | 0° | 0° | 90° |

Identifier séparément les axes du contrôleur de vol. Vérifier les angles réels avec un niveau / inclinomètre, puis laisser le banc immobile avant l’acquisition. Le centre de gravité et l’IMU ne sont pas nécessairement au même endroit.

## Vérification du prototype et limites pratiques

Commencer par les cadres seuls. Contrôler l’équerrage, la rotation libre, la tenue des goupilles et l’absence de fissures ou de blanchiment des pièces imprimées. Essayer ensuite une masse inerte maintenue, progressivement jusqu’à 2 kg, dans les six poses, sans laisser la charge sans surveillance. Contrôler le glissement des moyeux / bagues d’arrêt et le serrage après manipulation. La qualité d’impression, les couches, le fluage du PETG, la qualité du bois et le montage réel influencent directement la tenue.

À titre de calcul d’équilibrage, un drone de 2 kg décentré de 50 mm produit déjà environ 0,98 N·m sous gravité ; un pion placé à 45 mm du centre reçoit environ 22 N tangentiels pour ce seul couple. Les cadres et accessoires ajoutent leurs efforts. Ce calcul explique l’importance du réglage du centre de gravité ; il ne remplace pas une étude de résistance du montage imprimé.

La CAO contrôle les solides et des positions échantillonnées, pas les défauts d’impression, la résistance ou une trajectoire continue complète. Les essais couverts sont des poses manuelles statiques sans hélices. Ce banc n’est pas validé pour les poussées moteur, les vibrations, une boucle d’asservissement du drone ni une calibration de vitesse angulaire. La présence de métal impose aussi de traiter séparément les essais de magnétomètre.

## Contenu et modification des fichiers

Ouvrir `Banc_IMU_V2_Amateur_2kg.FCStd`. Les cellules B4, B5, B6 pilotent réellement toute la hiérarchie des trois axes. Les dimensions affichées sont des références ; les changements de structure se font dans `Construire_V2.FCMacro`, puis par reconstruction et nouveau contrôle.

Le groupe masqué « Pièces à imprimer » conserve la forme CAO de chaque pièce imprimée. Les STL sont orientés pour l’impression, tandis que ces formes de bibliothèque utilisent leurs coordonnées de conception. La macro lit les STEP fournisseur et les contours DXF présents dans Sources ; garder cette arborescence. La référence carbone est extrudée à 3 mm, épaisseur supposée faute de donnée explicite dans les contours utilisés.

Les fichiers JSON consignent les validations des solides, des maillages, des dimensions d’impression, des coupes et des positions. L’export STEP contient les pièces mécaniques visibles, sans le cylindre enveloppe masqué. Les vis, écrous de rainures et roulements ont des représentations simplifiées ; suivre la nomenclature pour le montage complet.
