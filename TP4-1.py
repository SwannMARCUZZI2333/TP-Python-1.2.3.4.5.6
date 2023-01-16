x = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

mult = [[0 for col in range(2)] for row in range(10)]

for i in range(10):
    mult[i][0] = i
    mult[i][1] = round(x * mult[i][0], 1)

for i in range(10):  
    print(f"{x} * {mult[i][0]} = {mult[i][1]}")