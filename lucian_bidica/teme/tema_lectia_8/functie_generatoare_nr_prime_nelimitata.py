from itertools import count


def functie_generatoare_numere_prime():
    for i in count():
        c = 0
        for j in range(2, i - 1):
            if i % j == 0:
                c += 1
        if c == 0:
            yield i


numerele_mele = iter(functie_generatoare_numere_prime())
while True:
    try:
        print(next(numerele_mele))
    except StopIteration:
        break
