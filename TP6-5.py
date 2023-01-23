import re

def clean(txt):
    alphachain = re.sub(r'[^a-zA-Z]', '', txt)
    alphachain = alphachain.lower()
    return alphachain

def special(specialchain):
    specialchain = re.sub(r'[éèêë]', 'e', specialchain)
    specialchain = re.sub(r'[àäâ]', 'a', specialchain)
    specialchain = re.sub(r'[öòô]', 'o', specialchain)
    specialchain = re.sub(r'[ïîì]', 'i', specialchain)
    specialchain = re.sub(r'[ûüù]', 'u', specialchain)
    specialchain = re.sub(r'[çÿñ]', 'c', specialchain)
    return specialchain

alpha_chain = clean(input("Entrez une chaine de caractères : "))
print(alpha_chain)

chain = special(alpha_chain)
print(chain)

death = 0
len_chain = len(chain)

for j in range(int(len_chain / 2)):
    if chain[j] != chain[len_chain - 1 - j]:
        print("Ce n'est pas un palindrome !")
        death = 1
        break

if death == 0:
    print("C'est un palindrome !")