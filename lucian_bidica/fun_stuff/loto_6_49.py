import time
from itertools import combinations


def extragere():
    for combinatie in combinations(range(1, 50), 6):
        yield combinatie


rezultate = iter(extragere())
contor = 0
t = time.process_time()
while True:
    try:
        print(next(rezultate))
        contor += 1
    except StopIteration:
        break
print("Pentru 6 din 49 sunt posibile ", contor, " variante de joc")
elapsed_time = time.process_time() - t
print("Processing time: ", elapsed_time, " secunde")

# Variantele cu extragere simpla random de 6 numere diferite
#
# import random
# lista_numere = []
# for i in range(1, 50):
#     lista_numere.append(i)
# lista_numere_extrase = []
# for i in range(6):
#     numar_extras = random.choice(lista_numere)
#     while numar_extras in lista_numere_extrase:
#         numar_extras = random.choice(lista_numere)
#     lista_numere_extrase.append(numar_extras)
# print(lista_numere_extrase)

# SAU
#
# numere = list(range(1,50))
# random.shuffle(numere)
# sase_numere = numere[:6]
# print(sase_numere)
