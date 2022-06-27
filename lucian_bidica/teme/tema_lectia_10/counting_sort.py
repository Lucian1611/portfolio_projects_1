from curs_grupa_python5.fisiere_cursanti.lucian_bidica.teme.tema_lectia_10.lista_random import lista_random
from modul_decorator_performanta import decorator_functie_performanta


@decorator_functie_performanta(name="Counting Sort")
def counting_sort(lista, val_max):
    nr_indici = val_max + 1
    count_nr = [0] * nr_indici

    for a in lista:
        count_nr[a] += 1
    k = 0
    for a in range(nr_indici):
        for c in range(count_nr[a]):
            lista[k] = a
            k += 1
    return lista


counting_sort(lista_random(), max(lista_random()))
