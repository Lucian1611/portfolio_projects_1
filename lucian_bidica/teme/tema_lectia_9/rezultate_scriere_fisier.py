import time


def decorator_function(function):
    def inner(*args, **kwargs):
        t1 = time.time()
        result = function(*args, **kwargs)
        t2 = time.time()
        timp_prelucrare = t2 - t1
        with open("fisier_nou.txt", "a") as o:
            o.write(f"Pentru prelucrarea a {num} de numere a fost nevoie de:")
            o.write("\n")
            o.write(f"{str(timp_prelucrare)} secunde \n")

        return result

    return inner

num = int(input("Cate numere in lista: "))
lista = []
for i in range(num):
    lista.append(i)


@decorator_function
def procesare_sortare(lista):
    lista = sorted(lista)
    return lista


procesare_sortare(lista)
