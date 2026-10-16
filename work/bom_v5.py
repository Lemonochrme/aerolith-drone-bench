from pathlib import Path
import csv,json
O=Path('outputs/V5_Helices_4K');rows=[]
def add(cat,desc,q,unit='pièce',note=''):
 rows.append([cat,desc,q,unit,note])
for sec,L,q,use in [('3030',280,4,'Demi-côtés tangage'),('3030',544,2,'Rails support drone'),('3030',560,2,'Côtés roulis'),('3030',620,2,'Traverses roulis'),('3030',720,2,'Traverses tangage'),('3030',940,4,'Socle et renforts'),('3030',1000,2,'Traverses socle'),('3030',120,1,'Indexeur de lacet'),('3060',600,2,'Montants'),('3060',950,1,'Traverse de fourche')]:add('Profilés',f'{sec} Type B rainure 8 — longueur {L} mm',q,note=use)
for desc,q,note in [('CP bouleau 250 × 250 × 18 mm, triangle rectangle',4,'CP03'),('CP bouleau 180 × 300 × 12 mm',1,'CP04 : support drone'),('CP bouleau 600 × 400 × 18 mm',1,'CP05 : socle pivot'),('CP bouleau disque Ø400 × 18 mm, trou Ø80',1,'CP06 : indexage lacet'),('Aluminium 80 × 200 × 3 mm',2,'AL01 : ponts de cadre'),('Aluminium 160 × 160 × 6 mm',2,'AL02 et AL03 : perçages différents'),('Aluminium 120 × 120 × 6 mm',1,'AL04 : pont de butée'),('Aluminium 160 × 240 × 6 mm',1,'AL05 : plateau tournant')]:add('Pièces plates',desc,q,note=note)
for desc,q,note in [('Équerre 30 B8 S8BBR30 avec kit 2 M6×12 + 2 écrous B8',26,'24 structure + 2 indexeur ; deux M6×12 et deux écrous B8 des kits restent inutilisés au pied fixé au bois'),('Roulement 6004-2RS — 20 × 42 × 12 mm',8,'Paliers tangage et roulis'),('Arbre acier lisse calibré Ø20 × 150 mm',4,'Tangage et roulis'),('Arbre acier lisse calibré Ø20 × 200 mm',1,'Lacet'),('Bague arrêt DIN 705 — 20 × 32 × 14 mm, vis incluse',9,'8 cardan + 1 lacet'),('Rondelle de réglage DIN 988 — 20 × 28 × 1 mm',16,'Appui sur bague intérieure des 6004'),('Palier à bride UCF204 Ø20, bride 86, entraxe 64 mm',2,'Vérifier fiche de la référence achetée'),('Butée à billes 51104 — 20 × 35 × 10 mm',1,'Ensemble avec ses deux rondelles'),('Support arbre SHF20, entraxe 47,5 mm',1,'Moyeu de lacet : respecter cet entraxe'),('Entretoise métallique traversante pour M4, L20 mm, Øext env.8',4,'Fixation drone au banc'),('Entretoise métallique traversante Øint8,5 mm, L12 mm',4,'Pont de butée ; longueurs identiques'),('Patin caoutchouc environ Ø36 × 15 mm',4,'Sous socle')]:add('Composants',desc,q,note=note)
bolts=[('Vis M6×16 tête cylindrique',28,'24 structure + 4 plateau de lacet'),('Vis M6×20 tête cylindrique',15,'12 structure + 3 indexeur'),('Vis M6×25 tête cylindrique',16,'12 goussets + 4 CP05'),('Vis M6×30 fraisée 90°',2,'SHF20 sur AL05 ; tête affleurante'),('Vis M6×35 tête cylindrique',2,'Pied indexeur sur CP05'),('Vis M6×35 moletée ou à oreilles',1,'Pion indexage lacet'),('Écrou rainure 8 Type B M6, hors kits',59,'Prévoir environ 70 ; en plus des kits des 26 équerres'),('Rondelle plate M6, hors kits',65,'Prévoir environ 80 ; larges aux appuis sur bois'),('Écrou M6 ordinaire',3,'2 SHF20 + 1 captif indexeur'),('Écrou frein M6',2,'Pied indexeur'),('Vis M4×55 tête cylindrique',12,'Paliers'),('Vis M4×65 tête cylindrique',4,'Paliers et bras indexage'),('Vis M4×45 tête cylindrique',4,'Fixation drone au banc'),('Écrou frein M4',20,'Paliers et fixation drone'),('Rondelle M4',40,'Sous têtes et écrous'),('Vis M5×60 tête cylindrique',12,'Moyeux et volants'),('Écrou M5 ordinaire, surplat 8 mm',12,'Logements imprimés'),('Rondelle M5',36,'28 cardan + 8 disque lacet'),('Vis M5×35 tête cylindrique ou moletée',2,'Indexage tangage et roulis'),('Vis M5×35 tête cylindrique',4,'Fixation disque lacet'),('Écrou papillon M5',2,'Indexage tangage et roulis'),('Écrou frein M5',4,'Fixation disque lacet'),('Tige filetée M10 longueur 170 mm',4,'Soit 680 mm finis ; une barre de 1 m suffit avec traits de scie'),('Vis hexagonale M10×50',4,'Palier lacet inférieur'),('Vis hexagonale M10×35',4,'Palier lacet supérieur'),('Écrou M10',40,'Tirants, contre-écrous et paliers'),('Rondelle M10',32,'Dont larges aux appuis sur bois'),('Vis M8×40',4,'Pont de butée'),('Écrou M8',4,'Pont de butée'),('Rondelle M8',8,'Pont de butée')]
for desc,q,note in bolts:add('Visserie hors kits',desc,q,note=note)
prints=json.load(open('outputs/V2_Amateur_2kg/verification_V2.json',encoding='utf-8'))['impressions']
for p in prints:add('Impression PETG',p['piece']+'.stl',p['quantite'],note=' × '.join(str(round(x,1)) for x in p['dimensions_impression_mm'])+' mm')
add('Impression PETG','10_Bras_index_lacet_x1.stl',1,note='110 × 50 × 48 mm')
with (O/'Liste_materiel_V5.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['Famille','Désignation','Quantité','Unité','Remarque']);w.writerows(rows)
text='''# Liste du matériel — banc IMU V5 pour drone de 2 kg

Nomenclature consolidée du banc V5 : parties hautes V2 et pivot de lacet V3. Les quantités sont les quantités montées, sauf indication de marge. Dimensions en mm. Cette liste remplace les listes V2/V3 séparées ; ne pas additionner les anciennes nomenclatures.

**22 coupes de profilés : 11,888 m de 3030 et 2,150 m de 3060.** Toute la famille doit être Type B, rainure 8. Longueurs finies : ajouter les traits de scie pour un achat en barres.

'''
for cat in dict.fromkeys(r[0] for r in rows):
 text+='## '+cat+'\n\n| Désignation | Qté | Remarque |\n|---|---:|---|\n'
 for c,d,q,u,n in rows:
  if c==cat:text+=f'| {d} | {q} | {n} |\n'
 text+='\n'
text+='''Les kits des 26 équerres fournissent 52 vis M6×12 et 52 écrous B8. Le montage en utilise 50 de chaque, les deux fixations au bois étant remplacées par les M6×35. Les 59 écrous B8 hors kits s'ajoutent donc à ces kits. Les rondelles fournies éventuellement dans les kits restent séparées des quantités hors kits.

Pour les assemblages métalliques, la nomenclature du pivot prévoit de la visserie acier classe 8.8 ; suivre les spécifications propres des composants achetés. Vis de blocage des paliers et des bagues à obtenir avec ces composants. Longueurs à contrôler avec les rondelles et pièces réelles avant commande en quantité.

## Impression et consommables

25 pièces montées + 1 coupon + 1 gabarit = **27 impressions, 12 formes STL**. Chaque forme tient sur un plateau 220 × 220 mm. PETG ; point de départ du dossier : buse 0,4 mm, couche 0,20 mm, 6 périmètres et remplissage 45–60 %, à adapter à la pièce. Quantité de filament à calculer dans le trancheur avec supports et bordures. Prévoir abrasif, consommables de perçage, lubrification de la butée selon sa notice et un maintien secondaire du drone adapté au châssis.

## Drone représenté dans la CAO — distinct des achats du banc

À réutiliser si le drone est déjà assemblé :

| Élément | Qté | Statut |
|---|---:|---|
| Platine centrale LithFrame | 2 | Contour DXF fourni ; carbone 3 mm supposé |
| Bras court LithFrame | 4 | Contour DXF fourni ; monté sur chant |
| Bras long LithFrame | 4 | Contour DXF fourni ; monté sur chant |
| Socle moteur LithFrame | 8 | Deux par moteur ; contour DXF fourni |
| Entretoise de châssis M3, longueur 20 | 4 | Représentation retenue pour l'assemblage |
| Moteur | 4 | Volume indicatif Ø28 × 20 + arbre ; référence à préciser |
| Hélice bipale | 4 | Représentation 9 pouces, 2 sens de chaque ; compatibilité réelle à définir |
| Batterie | 1 | Volume indicatif 36 × 100 × 38 |
| Contrôleur / électronique | 1 | Volume indicatif 36 × 36 × 7 |

La visserie complète du châssis, les fixations moteurs/hélices, les ESC, le récepteur, les câbles, connecteurs et sangles ne sont pas définis par les DXF. Cette partie n'est donc pas une nomenclature d'achat complète pour construire le drone. Les dimensions génériques des équipements ne servent pas à choisir des composants compatibles.

## Outillage

Profilés coupés à longueur ou scie adaptée ; scie sauteuse pour le bois ; perceuse à colonne de préférence, étau et serre-joints ; forets adaptés au bois et au métal, scies-cloches selon les plans ; fraise à 90° pour AL05 ; ébavureur, lime, pied à coulisse, équerre, clés Allen et clés plates. Niveau ou inclinomètre pour vérifier les angles de calibration.

## Plans et fichiers existants

Les STL sont dans `outputs/V3_Pivot_lacet/STL`. Les plans du pivot sont dans `outputs/V3_Pivot_lacet/Plans_pivot_V3.dxf`. Les plans des goussets, de la platine drone et des ponts AL01 sont dans le dossier V2. Ne plus acheter l'ancien roulement de plateau tournant Ø300, ni les panneaux CP01/CP02 : ils sont remplacés par la cartouche de lacet V3.

La présence d'hélices dans la visualisation V5 ne change pas l'usage de construction prévu : banc manuel de calibration statique, hélices retirées sur le drone réel. La structure n'est pas validée pour des essais de poussée moteur.
'''
(O/'Liste_materiel_V5.md').write_text(text,encoding='utf-8')
print('Lignes nomenclature:',len(rows));print('Impressions:',sum(p['quantite'] for p in prints)+1)
