limita = int(input("Introduceti valoarea limita: "))
lista = []
for i in range(2, limita + 1):
    lista.append(i)

for i in lista:
    for a in lista:
        if a != i and a % i == 0:
            lista.remove(a)
print(lista)
