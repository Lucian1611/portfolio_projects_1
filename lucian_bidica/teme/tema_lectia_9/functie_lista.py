lista_mea = ["Marian", "Roger", "Anna", "Razvan", "Petrica", "Darius", "Rodica", "Anton", "Rares"]
# lista_numere = [1, 6, 2, 3, -1, 4]


def functie_lista(lista):
    nume_r = []
    for i in lista:
        if i[0] == "R" or i[0] == "r":
            print(f'Numele: {i} incepe cu litera R')
            nume_r.append(i)
    nume_r_sortate = sorted(nume_r)
    return nume_r_sortate


print(""""Numele care incep cu litera R 
in ordine alfabetica sunt: """, functie_lista(lista_mea))
