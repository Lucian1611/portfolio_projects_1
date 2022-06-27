from curs_grupa_python5.fisiere_cursanti.lucian_bidica.teme.tema_lectia_10.lista_random import lista_random
from modul_decorator_performanta import decorator_functie_performanta


@decorator_functie_performanta(name="Insertion Sort")
def insertion_sort(lista):
    for i in range(len(lista) - 1):
        element1 = lista[i]
        element2 = lista[i + 1]
        if element2 < element1:
            index = 0
            for e in lista:
                if element2 < e:
                    index = lista.index(e)
                    break
            lista.insert(index, element2)
            lista.pop(i + 2)
    return lista


insertion_sort(lista_random())
