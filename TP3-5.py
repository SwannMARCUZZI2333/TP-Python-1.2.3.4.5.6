while True:
    debut = int(input("Donnez l’heure de début de la location (un entier) : "))
    if 0 <= debut <= 24:
        break
    else:
        print("Les heures doivent être comprises entre 0 et 24 !\n")

while True :
    fin = int(input("Donnez l’heure de fin de la location (un entier) : "))
    if 0 <= fin <= 24 and debut != fin:
        break
    elif debut == fin:
        print("Attention ! l’heure de fin est identique à l’heure de début.\n")
    #elif debut > fin:
    #   print("Attention ! le début de la location est après la fin ..."\n)
    else:
        print("Les heures doivent être comprises entre 0 et 24 !\n")

tab = [0] * 24
high = 0
low = 0

if debut < fin:                 # commentable
    for i in range(debut, fin):
        tab[i] = 1
else:                           # commentable
    for i in range(debut, 24):  # commentable
        tab[i] = 1              # commentable
    for i in range(0, fin):     # commentable
        tab[i] = 1              # commentable

for i in range(24):
    if 7 <= i < 17:
        high = high + tab[i]
    else:
        low = low + tab[i]

pay = float(high * 2 + low)

print(f"Vous avez loué votre vélo pendant :")
if low != 0:
    print(f"{low} heure(s) au tarif horaire de 1.0 euro")
if high != 0:
    print(f"{high} heure(s) au tarif horaire de 2.0 euros")
print(f"Le montant total à payer est de {pay} euro(s).")