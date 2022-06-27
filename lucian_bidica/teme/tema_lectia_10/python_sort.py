from curs_grupa_python5.fisiere_cursanti.lucian_bidica.teme.tema_lectia_10.lista_random import lista_random
from modul_decorator_performanta import decorator_functie_performanta


@decorator_functie_performanta(name="Timsort Sort")
def sortare(lista):
    lista_sortata = sorted(lista)
    return lista_sortata



sortare(lista_random())
