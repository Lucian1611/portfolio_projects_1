from curs_grupa_python5.fisiere_cursanti.lucian_bidica.teme.tema_lectia_10.lista_random import lista_random
from curs_grupa_python5.fisiere_cursanti.lucian_bidica.teme.tema_lectia_10.modul_decorator_performanta import \
    decorator_functie_performanta


def merge_sort(lista):
    lungime_lista = len(lista)
    if lungime_lista == 1:
        return lista

    mijloc = lungime_lista // 2
    bucata_stanga = merge_sort(lista[:mijloc])
    bucata_dreapta = merge_sort(lista[mijloc:])
    return merge(bucata_stanga, bucata_dreapta)


def merge(stanga, dreapta):
    lista_sortata = []
    i = j = 0

    while i < len(stanga) and j < len(dreapta):

        if stanga[i] < dreapta[j]:

            lista_sortata.append(stanga[i])

            i += 1
        else:
            lista_sortata.append(dreapta[j])
            j += 1
    lista_sortata.extend(stanga[i:])
    lista_sortata.extend(dreapta[j:])

    return lista_sortata


@decorator_functie_performanta(name="Merge Sort")
def run_merge_sort(lista):
    sorted_list = merge_sort(lista)
    return sorted_list


run_merge_sort(lista_random())
