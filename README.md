# aerolith-drone-bench
Test bench for Aerolith Drone

<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/534f0bd1-af26-4b2a-938c-14c92124e17a" />

# Banc de calibration IMU / test multiaxe LithFrame F380

Projet FreeCAD pour un banc manuel multiaxe, conçu autour d'un drone complet de 2 kg et de pièces imprimables sur un plateau de 220 × 220 mm.

## Version actuelle

- CAO : `outputs/V5_Helices_4K/Banc_IMU_V5_Helices.FCStd`
- Échange STEP : `outputs/V5_Helices_4K/Banc_IMU_V5_Helices.step`
- Animation 4K : `outputs/V5_Helices_4K/Banc_IMU_Helices_4K.mp4`
- Nomenclature : `outputs/V5_Helices_4K/Liste_materiel_V5.md` et `.csv`
- Pièces imprimables : `outputs/V3_Pivot_lacet/STL/`
- Notice du pivot et plans : `outputs/V3_Pivot_lacet/`
- DXF originaux du drone : `outputs/Sources_LithFrame/`

Les dossiers de versions précédentes sont conservés pour retrouver les plans, les macros et les étapes de conception. La nomenclature V5 consolide les achats et remplace l'addition des listes précédentes.

## Utilisation

Ouvrir la CAO V5 dans FreeCAD. Les cellules B4, B5 et B6 du tableau Parametres pilotent le lacet, le tangage et le roulis. Les équipements et hélices du drone sont des représentations indicatives lorsque les modèles réels n'ont pas été fournis.

Usage prévu : calibration manuelle statique, hélices retirées sur le drone réel. Les contrôles géométriques ne constituent pas une validation de résistance ni une autorisation d'essais de poussée moteur.

Les scripts de construction, de rendu et de nomenclature sont conservés dans `work/`. Certains utilisent les chemins Windows et la connexion RPC FreeCAD de l'environnement de création ; ils doivent être adaptés avant exécution sur un autre poste. Les fichiers CAO livrés s'ouvrent directement.
