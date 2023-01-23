somme = int(input("Entrez la somme d'argent à décomposer : "))

billet_100 = somme // 100
reste = somme % 100

billet_50 = reste // 50
reste = reste % 50

billet_10 = reste // 10
reste = reste % 10

piece_2 = reste // 2
reste = reste % 2

piece_1 = reste

print(f"{somme} euros, c'est donc {billet_100} billets de 100, {billet_50} de 50, {billet_10} de 10, {piece_2} pièces de 2 et {piece_1} pièce 1.")