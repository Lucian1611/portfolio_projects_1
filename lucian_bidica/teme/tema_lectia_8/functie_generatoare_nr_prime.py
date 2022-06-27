import time


def functie_generatoare_numere_prime(valoare):
    t = time.process_time()
    for i in range(1, valoare):
        c = 0
        for j in range(2, i):
            if i % j == 0:
                c += 1
        if c == 0:
            yield i
    elapsed_time = time.process_time() - t
    print("Processing time: ", elapsed_time, " secunde")


val = int(input("Până la ce valoare sa afișăm numere prime: "))
numerele_mele = iter(functie_generatoare_numere_prime(val))
numaratoare = 0
while True:
    try:
        print(next(numerele_mele))
        numaratoare += 1
    except StopIteration:
        break
print(f" in intervalul 0 - {val}, s-au găsit {numaratoare} numere prime")
