
nb=int(input("Entrez un nombre entier:?"))
if nb==0:
    print(nb,"est nul")
else:
    if nb>0 and nb%2 ==0:
        print(nb,"est positif et pair") 
    else:
        if nb>0 and nb%2 !=0:
            print(nb,"est positif et impair")
        else:
            if nb<0 and nb%2 ==0:
                print(nb,"est negatif et impair")
            else: 
                print(nb,"est negatif et impair")



   