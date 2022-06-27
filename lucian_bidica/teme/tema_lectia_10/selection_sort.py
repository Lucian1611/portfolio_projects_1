from curs_grupa_python5.fisiere_cursanti.lucian_bidica.teme.tema_lectia_10.lista_random import lista_random
from modul_decorator_performanta import decorator_functie_performanta


@decorator_functie_performanta(name="Selection Sort")
def selection_sort(lista):
    lista_sortata = []
    while len(lista) > 0:
        minimum = min(lista)
        lista_sortata.append(minimum)
        lista.remove(minimum)
    return lista_sortata


selection_sort(lista_random())
