import random

rand = random.randrange(0, 101, 1)
print(rand) # Affiche le nombre aléatoire
i = 0
x = rand + 1

while x != rand:
    x = int(input("Devinez le nombre aléatoire : "))
    i = i + 1
    if x == rand:
        print(f"Vous avez trouvez le nombre aléatoire en {i} essai(s).")
    elif x < rand:
        print("Votre nombre est inférieur au nombre aléatoire.")
    else:
        print("Votre nombre est supérieur au nombre aléatoire.")