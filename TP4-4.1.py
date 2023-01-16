L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
counter = [0] * len(L1)
val = 0
high = 0
amount = 0

for i in range(len(L1)):
    for j in L1:
        if L1[i] == j:
            counter[i] = counter[i] + 1

for k in range(len(counter)):
    if counter[k] > val:
        val = counter[k]

for l in range(len(counter)):
    if counter[l] == val:
        high = L1[l]
        amount = counter[l]
        break
print(f"Le nombre le plus frequent dans la liste est le : {high} ({amount} x)")

