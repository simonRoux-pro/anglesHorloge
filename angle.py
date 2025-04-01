def calculer_angle(h, m, s):
    if h < 0 or h > 12 or m < 0 or m >= 60 or s < 0 or s >= 60:
        raise ValueError("Heure, minute ou seconde invalide")
    
    # Calcul de l'angle de l'aiguille des heures
    angle_heures = (30 * h) + (m * 0.5) + (s * (0.5 / 60))
    
    # Calcul de l'angle de l'aiguille des minutes
    angle_minutes = (6 * m) + (s * 0.1)
    
    # Calcul de l'angle de l'aiguille des secondes
    angle_secondes = 6 * s
    
    # Calcul de l'angle absolu entre l'aiguille des heures et celle des minutes
    angle_hm = abs(angle_heures - angle_minutes)
    angle_hm = min(angle_hm, 360 - angle_hm)
    
    # Calcul de l'angle absolu entre l'aiguille des minutes et celle des secondes
    angle_ms = abs(angle_minutes - angle_secondes)
    angle_ms = min(angle_ms, 360 - angle_ms)
    
    # Calcul de l'angle absolu entre l'aiguille des heures et celle des secondes
    angle_hs = abs(angle_heures - angle_secondes)
    angle_hs = min(angle_hs, 360 - angle_hs)
    
    return angle_hm, angle_ms, angle_hs

# Exemple d'utilisation
heure = int(input("Entrez l'heure (0-12) : "))
minute = int(input("Entrez les minutes (0-59) : "))
seconde = int(input("Entrez les secondes (0-59) : "))

try:
    angle_hm, angle_ms, angle_hs = calculer_angle(heure, minute, seconde)
    print(f"L'angle entre l'aiguille des heures et des minutes est de {angle_hm:.2f} degrés.")
    print(f"L'angle entre l'aiguille des minutes et des secondes est de {angle_ms:.2f} degrés.")
    print(f"L'angle entre l'aiguille des heures et des secondes est de {angle_hs:.2f} degrés.")
except ValueError as e:
    print(e)
