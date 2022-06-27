import random


def lista_random():
    lista_mea = []
    for i in range(22500):
        n = random.randint(-50000, 50000)
        lista_mea.append(n)
    return lista_mea