n = int(input("Entrez un entier : "))

choice = 0
while True:
    choice = int(input("Entrez 1 pour 'for' ou 2 pour 'while' : "))
    if choice == 1 or choice == 2:
        break

print(f"Evolution de la valeur de la factorielle de {n} :")

fact = 1
print(f" 0) {fact}")

if choice == 1 and n != 0: # Boucle for
    for i in range(n):
        fact = fact * (i + 1)
        print(f" {i + 1}) {fact}")

elif n != 0:  # Boucle while
    i = 1
    while i != (n + 1):
        fact = fact * (i)
        print(f" {i}) {fact}")
        i = i + 1

print(f"La factorielle de {n} est {fact}.")