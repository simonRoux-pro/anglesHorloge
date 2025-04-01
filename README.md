# Calcul de l'angle des aiguilles d'une horloge

## Description
Ce projet permet de calculer l'angle entre les aiguilles d'une horloge analogique en fonction des heures, minutes et secondes fournies par l'utilisateur.

## Formules utilisées

### Angle de l'aiguille des heures par rapport à 12h00 :
```math
A_h = 30 \times H + 0.5 \times M + \frac{S}{120}
```
- Chaque heure représente 30°.
- Chaque minute fait avancer l'aiguille des heures de 0.5°.
- Chaque seconde fait avancer l'aiguille des heures de 1/120°.

### Angle de l'aiguille des minutes par rapport à 12h00 :
```math
A_m = 6 \times M + 0.1 \times S
```
- Chaque minute représente 6°.
- Chaque seconde fait avancer l'aiguille des minutes de 0.1°.

### Calcul de l'angle entre les aiguilles des heures et des minutes :
```math
\theta = |A_h - A_m|
```
L'angle minimal est obtenu par :
```math
\theta_{min} = \min(\theta, 360 - \theta)
```

## Exemple de calcul
Pour **3h15min30s** :
- `A_h = 97.75°`
- `A_m = 93°`
- `θ = 4.75°`

## Utilisation du script
### Prérequis
- Python 3 installé sur votre machine

### Exécution du script
```bash
python angle.py
```

### Exemple de sortie
```
Entrez l'heure (0-12) : 3
Entrez les minutes (0-59) : 15
Entrez les secondes (0-59) : 30
L'angle entre l'aiguille des heures et des minutes est de 4.75 degrés.
L'angle entre l'aiguille des minutes et des secondes est de 87.00 degrés.
L'angle entre l'aiguille des heures et des secondes est de 82.25 degrés.
```

## Auteur
Simon Roux