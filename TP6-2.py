lst1 = [0, 1, 2]

def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst
lst =[0, 1, 2]
lst_2 = ajouter_elt(lst1, len(lst1))
print("lst1: ", lst1)
print("Type de lst1: ", type(lst1))
print("Id de lst1: ", id(lst1))
print("lst2: ", lst_2)
print("Type de lst2: ", type(lst_2))
print("Id de lst2: ", id(lst_2))