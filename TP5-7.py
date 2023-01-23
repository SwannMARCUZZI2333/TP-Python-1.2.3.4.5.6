import os
from datetime import datetime

nom_fichier1 = input("Entrez le nom du premier fichier : ")
nom_fichier2 = input("Entrez le nom du deuxième fichier : ")

if os.path.isfile(nom_fichier1):
    taille1 = os.path.getsize(nom_fichier1)
    date_modification1 = datetime.fromtimestamp(os.path.getmtime(nom_fichier1))
    print(f"Le fichier {nom_fichier1} existe, sa taille est de {taille1} octets et a été modifié le {date_modification1}.")
else:
    print(f"Le fichier {nom_fichier1} n'existe pas.")

if os.path.isfile(nom_fichier2):
    taille2 = os.path.getsize(nom_fichier2)
    date_modification2 = datetime.fromtimestamp(os.path.getmtime(nom_fichier2))
    print(f"Le fichier {nom_fichier2} existe, sa taille est de {taille2} octets et a été modifié le {date_modification2}.")
else:
    print(f"Le fichier {nom_fichier2} n'existe pas.")

if os.path.isfile(nom_fichier1) and os.path.isfile(nom_fichier2):
    if date_modification1 > date_modification2:
        print(f"Le fichier {nom_fichier1} est plus récent.")
    elif date_modification1 < date_modification2:
        print(f"Le fichier {nom_fichier2} est plus récent.")
    else:
        print(f"Les fichiers {nom_fichier1} et {nom_fichier2} ont la même date de modification.")