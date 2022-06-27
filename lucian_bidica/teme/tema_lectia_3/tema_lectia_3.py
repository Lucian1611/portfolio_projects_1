#Rezolvare Tema Lectia 3
import time

# 1. Fiind data o lista de numere, sa se extraga multiplii de 3, 5, 7 intr-o alta lista.
nr_elemente_lista = int(input("Cate numere doriti sa includeti in lista? : "))
lista = []
i = 0
while i <= nr_elemente_lista - 1:
    element_lista = int(input("Introduceti un numar:"))
    lista.append(element_lista)
    i += 1
print("lista este: ", lista)
lista1=[]
print("Mai jos sunt listati multiplii numerelor 3, 5, sau 7")
for i in lista:
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        lista1.append(i)
    i += 1
print(lista1)
print("------------------------------Exercitiul 2--------------------------------")
time.sleep(2)


# 2. Fiind data o lista de dicționare cu produse de tipul: {"nume":"branza hochland", "pret": 14.2}, sa se genereze o alta lista
#    care sa conțină doar produsele cu prețul între min=15.23 si max=37.75
#(aici am creat doar un dicționar, nu o lista de dictionare)
dict = {"ardei": 43.23,
         "ceapa": 23.02,
         "rosii": 15.42,
         "castraveti": 67.01,
         "bere": 14.32,
         "suc": 33.33,
         "lapte": 20.20}
for key, value in dict.items():
    print(key, value)
print("Produsele care se încadrează în intervalul de preț dorit: ")
for k, v in dict.items():
    if 15.23 <= v <= 37.75:
        print(k, v)
print("------------------------------Exercitiul 3--------------------------------")
time.sleep(2)


# 3. Fiind dat un string, sa se verifice daca este palindrom.
pal = input("Introduceți un număr/șir de caractere pentru a verifica dacă este palindrom: ")
w = ""
for i in pal:
    w = i + w
if (pal == w):
    print("numărul/șirul de caractere ESTE palindrom")
else:
    print("Numărul/șirul de caractere NU ESTE palindrom!")
print("------------------------------Exercitiul 4--------------------------------")
time.sleep(2)


# 4. Fiind data o lista cu numere, sa se afiseze doar cele ale căror suma a cifrelor este egala cu 3
nr_elemente_lista = int(input("Cate numere doriti sa includeti in lista? : "))
lista = []
i = 0
while i <= nr_elemente_lista - 1:
    element_lista = int(input("Introduceti un numar:"))
    lista.append(element_lista)
    i += 1
print("lista este: ", lista)
print("Numerele ale căror suma a cifrelor este mai mica decat 3 sunt: ")
for i in lista:
    num_str = str(i)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    if sum==3:
        print(num_str, end=" ")
print()
print("------------------------------Exercitiul 5--------------------------------")
time.sleep(2)


# 5. Fiind data o lista cu duplicate, sa se elimine duplicatele.
nr_elemente_lista = int(input("Cate elemente (substantive) doriti sa includeti in lista? : "))
lista = []
i = 0
while i <= nr_elemente_lista - 1:
    element_lista = input("Introduceti un substantiv:")
    lista.append(element_lista)
    i += 1
print("Lista initiala: ", lista)
lista_fara_duplicate = []
for i in lista:
    if i not in lista_fara_duplicate:
        lista_fara_duplicate.append(i)
print("Lista fara duplicate: ")
print(lista_fara_duplicate)
print("------------------------------Exercitiul 6--------------------------------")
time.sleep(2)


# 6. Fiind data o lista cu numere, sa se afiseze valorile prime din lista
nr_elemente_lista = int(input("Cate numere doriti sa includeti in lista? : "))
lista = []
i = 0
while i <= nr_elemente_lista - 1:
    element_lista = int(input("Introduceti un numar:"))
    lista.append(element_lista)
    i += 1
print("lista este: ", lista)
lista_numere_prime = []
for i in lista:
    c = 0
    for j in range(2,i//2):
        if i % j == 0:
            c += 1
    if c == 0:
        lista_numere_prime.append(i)
print("Numerele prime din lista dumneavoastra sunt: ")
print(lista_numere_prime)
print("------------------------------Exercitiul 7--------------------------------")
time.sleep(2)


# 7. Cu dimensiunea bazei luată dintr-o variabila,
# a) Sa se afiseze in terminal o jumatate de brad de forma următoare
# #
# ##
# ###
# ####
# #####
# ######
baza = int(input("Introduceți dimensiunea bazei: "))
for i in range(1, baza):
    print("#" * i)
    i = i + 1
print("---------------------------------------------------------")
# b) Sa se afiseze un brad de forma:
#      #
#     ###
#    #####
#   #######
#  #########
# ###########
j = 1
k = baza // 2
while j <= baza:
    print("  " * k, "#" * j, " " * k)
    j += 2
    k -= 1
print("---------------------------------------------------------")
# c) Sa se afișeze un brad cu background de forma:
# ^^^^ # ^^^^
# ^^^ ### ^^^
# ^^ ##### ^^
# ^ ####### ^
#  #########
# ###########
j = 1
k = baza // 2
while j <= baza:
    print(" ^" * k, "#" * j, " ^" * k)
    j += 2
    k -= 1
