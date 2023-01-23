notes = []
somme = 0
coefficients = []

for i in range(5):

    s = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ")
    note, coef = s.split(" ")
    note = float(note)
    coef = int(coef)

    if note < 8:
        print("Note inférieure à 8, étudiant échoue.")
        exit()

    notes.append(note)
    coefficients.append(coef)
    somme += note*coef

moyenne = somme / sum(coefficients)
print(round(moyenne, 2))

if moyenne > 10:
    print("Moyenne générale supérieure à 10, étudiant admis.")
else:
    print("Moyenne générale inférieure à 10, étudiant non admis.")