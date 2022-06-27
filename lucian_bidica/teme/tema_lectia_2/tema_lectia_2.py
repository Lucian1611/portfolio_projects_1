#Rezolvare Tema Lectia 2
import time

# 1. Fiind dat nu numar de la tastatura, sa se afle toti divizorii lui.
print("Exercitiul nr. 1: ")
nr = int(input("Introduceti un numar pentru a-i afla toti divizorii: "))
i = 1
while i <= nr:
    if nr % i == 0:
        print(nr, "este divizibil cu", i)
    i = i + 1

# 2. Fiind dat un numar intreg, sa se afiseze cate cifre are.
time.sleep(2)
print("Exercitiul nr. 2: Prima varianta de rezolvare: ")
numar = input("Introduceti un numar pentru a vedea din cate cifre este compus: ")
print("Numarul introdus de dumneavoastra este compus din: ", len(numar), "cifre")

# SAU

time.sleep(2)
print("Exercitiul nr. 2/ A doua varianta de rezolvare: ")
num = int(input("Introduceti un numar pentru a verifica din cate cifre este alcatuit"))
if num >= 10:
    count = 2
else:
    count = 1
while num // 10 > 9:
    count += 1
    num = num // 10
print("Numarul introdus de dumneavoastra este compus din: ", count, "cifre")

# 3. Sa se genereze primele 50 de numere naturale divizibile cu 7.
time.sleep(2)
print("Exercitiul nr. 3: ")
print("Primii 50 de multiplii ai numarului 7 sunt: ")
i = 1
while i <= 50:
    a = i * 7
    print(a, end=" ")
    i += 1

# 4. Fiind citite 3 valori de la tastatura: zi, luna, an, sa se fac validarile:
# pentru fiecare luna in parte, ziua sa fie valoare valida.
# bouns points pentru ani bisecti (feb=29 zile).
time.sleep(2)
print("Exercitiul nr. 4: ")
zi = int(input("Introduceti ziua: "))
while zi > 31:
    print("Ati introdus o valoare gresita pentru zi!")
    zi = int(input("Introduceti ziua: "))
luna = int(input("Introduceti luna: "))
while luna > 12:
    print("Ati introdus o valoare gresita pentru luna!")
    luna = int(input("Introduceti luna: "))
an = int(input("Introduceti anul: "))
while an <= 1900:
    print("Ati introdus o valoare gresita pentru an!")
    an = int(input("Introduceti anul: "))
print("Data introdusa de dumneavoastra este:", zi, " ", luna, " ", an)
if luna == 4 or luna == 6 or luna == 9 or luna == 11:
    if zi > 30:
        print("Data introdusa NU ESTE valida!")
    else:
        print("Data introdusa ESTE valida!")
if luna == 2:
    if an % 4 != 0:
        if zi > 28:
            print("Data introdusa NU ESTE valida!")
        else:
            print("Data ESTE valida!")
    elif an % 4 == 0:
        if zi > 29:
            print("Data introdusa NU ESTE valida!")
        else:
            print("Data ESTE valida!")
if luna==1 or luna==3 or luna==5 or luna==7 or luna==10 or luna ==12:
    print("Data ESTE valida!")

# 5. Sa se verifice daca un numar este palindrom.
time.sleep(2)
print("Exercitiul nr. 5: ")
pal = input("Introduceti un numar/sir de caractere pentru a verifica daca este palindrom:")
w = ""
for i in pal:
    w = i + w
if (pal == w):
    print("numarul/sirul de caractere ESTE palindrom")
else:
    print("Numarul/sirul de caractere NU ESTE palindrom!")

# 6. Fiind date 2 puncte in 3 dimensiuni (pt = x, y, z),
# sa se afiseze coordonatele mijlocului segmentului de dreapta dintre cele 2 puncte.
time.sleep(2)
print("Exercitiul nr. 6: ")
print("Introduceti coordonatele x, y si z pentru primul punct:")
x = int(input())
y = int(input())
z = int(input())
print("Introduceti coordonatele x1, y1 si z1 pentru al doilea punct:")
x1 = int(input())
y1 = int(input())
z1 = int(input())
x2 = (x + x1) / 2
y2 = (y + y1) / 2
z2 = (z + z1) / 2
print("Coordonatele mijlocului segmentului de dreapta determinat de punctele A si b sunt: x=", x2, "y=", y2, "z=", z2)

# 7. Fiind dat un CNP de la tastatura, sa se valideze. (https://contabcaf.blogspot.com/2012/11/algoritm-de-validare-pentru-cnp.html)
time.sleep(2)
print("Exercitiul nr. 7 / Prima varianta de rezolvare: ")
cnp = int(input("Introduceti va rugam un CNP:"))
while len(str(cnp)) !=13:
    print("Ati introdus un CNP gresit:")
    cnp = int(input("Introduceti va rugam un CNP:"))
numar_de_control_introdus = cnp % 10
cnp = ((cnp - cnp % 10) / 10)
a = cnp % 10 * 9
cnp = ((cnp - cnp % 10) / 10)
b = cnp % 10 * 7
cnp = ((cnp - cnp % 10) / 10)
c = cnp % 10 * 2
cnp = ((cnp - cnp % 10) / 10)
d = cnp % 10 * 8
cnp = ((cnp - cnp % 10) / 10)
e = cnp % 10 * 5
cnp = ((cnp - cnp % 10) / 10)
f = cnp % 10 * 3
cnp = ((cnp - cnp % 10) / 10)
g = cnp % 10 * 6
cnp = ((cnp - cnp % 10) / 10)
h = cnp % 10 * 4
cnp = ((cnp - cnp % 10) / 10)
i = cnp % 10 * 1
cnp = ((cnp - cnp % 10) / 10)
j = cnp % 10 * 9
cnp = ((cnp - cnp % 10) / 10)
k = cnp % 10 * 7
cnp = ((cnp - cnp % 10) / 10)
l = cnp % 10 * 2
numar_de_control_obtinut = (a + b + c + d + e + f + g + h + i + j + k + l) % 11
if numar_de_control_obtinut < 10:
    if numar_de_control_introdus == numar_de_control_obtinut:
        print("Ati introdus un CNP Valid!")
    else:
        print("CNP-ul introdus NU ESTE valid!")
else:
    numar_de_control_obtinut = 1
    if numar_de_control_obtinut == numar_de_control_introdus:
        print("Ati introdus un CNP Valid!")
    else:
        print("CNP-ul introdus NU ESTE valid!")

# SAU

time.sleep(2)
print("Exercitiul nr. 7/ A doua varianta de rerzolvare:  ")
cnp = input("Introduceti CNP-ul: ")
while len(str(cnp)) !=13:
    print("Ati introdus un CNP gresit:")
    cnp = input("Introduceti va rugam un CNP:")
a = int(cnp[0]) * 2
b = int(cnp[1]) * 7
c = int(cnp[2]) * 9
d = int(cnp[3]) * 1
e = int(cnp[4]) * 4
f = int(cnp[5]) * 6
g = int(cnp[6]) * 3
h = int(cnp[7]) * 5
i = int(cnp[8]) * 8
j = int(cnp[9]) * 2
k = int(cnp[10]) * 7
l = int(cnp[11]) * 9
cifra_control_introdusa = int(cnp[12])
cifra_control_obtinuta = (a + b + c + d + e + f + g + h + i + j + k + l) % 11
if cifra_control_obtinuta < 10:
    if cifra_control_introdusa == cifra_control_obtinuta:
        print("CNP-ul introdus ESTE valid!")
    else:
        print("CNP-ul introdus NU ESTE valid!")
else:
    cifra_control_obtinuta = 1
    if cifra_control_introdusa == cifra_control_obtinuta:
        print("CNP-ul introdus ESTE valid!")
    else:
        print("CNP-ul introdus NU ESTE valid!")

# 8. Fiind dat un pret, o cantitate totala de produse, si un index n
#    pentru fiecare al n-lea produs redus in cos.
#    Toate produsele din cos sunt de acelasi pret.
#    Pentru reducere se aplica un procent intreg intre 0 si 100 la fiecare al n-lea element.
#    Sa se calculeze valoarea cosului.
time.sleep(2)
print("Exercitiul nr. 8: ")
pret = int(input("Introduceti pretul produselor: "))
nr_produse = int(input("Introduceti numarul de produse:"))
index_pt_reducere = int(input("Introduceti pentru al catelea produs cumparat se face reducerea:"))
procent_reducere = int(input("Introduceti procentul (%) de reducere aplicat: "))
valoare_totala = pret * nr_produse
nr_produse_reduse = nr_produse // index_pt_reducere
reducere = nr_produse_reduse * procent_reducere / 100 * pret
valoare_cos = valoare_totala - reducere
print("Cosul dumneavoastra contine:", nr_produse, " produse in valoare totala de:", valoare_totala, "lei")
print("Valoarea de plata a cosului dumneavoastra este de: ", valoare_cos, "lei. Aveti o REDUCERE totala de: ", reducere,
      "lei")
