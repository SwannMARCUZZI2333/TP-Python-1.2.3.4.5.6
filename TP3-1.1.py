while True:
    n = int(input("Entrer un nombre entier naturel : "))
    if n >= 0:
        break

sum = 0
i = 0

for i in range(n+1):
    sum = sum + i

print(f"La somme des {n} entiers naturels est {sum}")