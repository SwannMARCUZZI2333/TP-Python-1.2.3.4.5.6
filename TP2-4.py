Base=4
fromage=800.0
eau=2
ail=2
pain=400

nbConvives= int(input("nombre de convives?"))


nvFromage=(fromage*nbConvives/Base)
nveau=(eau*nbConvives/Base)
nvail=(ail*nbConvives/Base)
nvpain=(pain*nbConvives/Base)

print(nvFromage,"gr de fromage")
print(nveau,"L d'eau")
print(nvail,"gousse d'ail")
print(nvpain,"gr de pain")