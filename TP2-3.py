a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")

tmp1=a
tmp2=b
tmp3=c

a=tmp2
b=tmp3
c=tmp1


print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)