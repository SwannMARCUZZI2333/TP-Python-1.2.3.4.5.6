i = 0
count10 = 0
count15 = 0
count20 = 0
tab = [0] * 10

for i in range(10):
    while True:
        tab[i] = int(input("Entrez un réel entre 0 et 20 : "))
        if 0 <= tab[i] <= 20:
            break
        else:
            print("Mauvaise valeur saisie, réessayez !")

    if tab[i] < 10:
        count10 = count10 + 1
    elif tab[i] < 15:
        count15 = count15 + 1
    else:
        count20 = count20 + 1

print(f"Le nombre de valeurs inférieur strictement à 10 est : {count10}\n"
      f"Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est : {count15}\n"
      f"Le nombre de valeurs supérieur ou égale à 15 est : {count20}")