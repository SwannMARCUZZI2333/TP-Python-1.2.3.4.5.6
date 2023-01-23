import re

def detect_palyndrome(s):

    s = re.sub(r'[^a-zA-Z]+', '', s)
    s = s.lower()
    return s == s[::-1] 
string = input("Entrez une chaine de caractères : ")

if detect_palyndrome(string):
    print("La chaîne épurée est un palindrome.")
else:
    print("La chaîne épurée n'est pas un palindrome.")
