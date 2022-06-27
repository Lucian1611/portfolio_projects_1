lista = ["Marius", "Andrei", "Flavius", "Anna", "Lucian", "Robert", "Luca"]
lista2 = [1, 4, 5, 7, 10, 2, -4]


def functie_sortare(lista):
    lista = sorted(lista)
    return lista


print(functie_sortare(lista2))


def functie_sortare2(lista):
    lista = lista.sort()
    return lista


functie_sortare2(lista2)
print(lista2)
