from curs_grupa_python5.fisiere_cursanti.lucian_bidica.teme.tema_lectia_10.lista_random import lista_random
from modul_decorator_performanta import decorator_functie_performanta


@decorator_functie_performanta(name="Bubble Sort")
def bubble_sort(lista):
    sortat = False
    while not sortat:
        sortat = True
        for i in range(len(lista) - 1):
            element_i = lista[i]
            element_ii = lista[i + 1]
            if element_i > element_ii:
                lista[i] = element_ii
                lista[i + 1] = element_i
                sortat = False
    return lista


bubble_sort(lista_random())
