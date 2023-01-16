jour = int(input("donner un nombre de jour:"))
heure= int(input("donner un nombre d'heure:"))
minute= int(input("donner un nombre de minute:"))

jourminute= (jour*1440)
heureminute= (heure*60)
minutetotal= (minute+heureminute+jourminute)

print (minutetotal)