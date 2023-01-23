heures_travaillées = int(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire_base = min(heures_travaillées, 160) * salaire_horaire

heures_supplementaires = max(heures_travaillées - 160, 0)

salaire_maj1 = 0
salaire_maj2 = 0

if heures_supplementaires > 0:
    salaire_maj1 = (min(heures_supplementaires, 40) * salaire_horaire * 1.25)
    heures_supplementaires -= 40

if heures_supplementaires > 0:
    salaire_maj2 = (heures_supplementaires * salaire_horaire * 1.50)

salaire_total = salaire_base + salaire_maj1 + salaire_maj2

print(f"Le salaire de l'ouvrier est de {salaire_total:.2f} euros.")