import time

choice = 0
while True:
    choice = int(input("Entrez 1 pour 'for' ou 2 pour 'while' : "))
    if choice == 1 or choice == 2:
        break

n = -1
while n < 0:
    n = int(input("Saisissez un nombre entier positif : "))

print(f"Les nombres par ordre décroissant entre {n} et 0 sont :")

if choice == 1: # Boucle for
    i = 0
    for i in range(n + 1):
        print(n - i)
        time.sleep(0.2)

else: # Boucle while
    while n >= 0:
        print(n)
        n = n - 1
        time.sleep(0.2)