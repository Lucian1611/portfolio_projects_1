#Rezolvare Tema Lectia 1
# se afisaza textul: "Python is cool :)"
import time

print("Python is cool :) ")
time.sleep(3)

# se afisaza: un intreg
print("Se afisaza un numar intreg:")
time.sleep(2)
print(20)
time.sleep(3)

#  se afisaza: un Nontype
# (AICI NU SUNT SIGUR CA AM INTELES- AM AFISAT CLASA: "NONTYPE")
print("Se afisaza un NonType: ")
time.sleep(2)
x = None
print(type(x))
time.sleep(3)

# se afisaza: un string
print("Se afisaza un string:")
time.sleep(2)
print("Lucian e tare!")
time.sleep(3)

# se afisaza: un boolean
print("Se afisaza boolean:")
time.sleep(2)
inclus = "a" in "Lucian"
print(inclus)
time.sleep(3)

# se introduc la alegere trei numere apoi calculatorul va afisa media lor aritmetica
m = int(input("Introduceti primul numar pentru media aritmetica: "))
n = int(input("Introduceti al doilea numar pentru media aritmetica: "))
o = int(input("Introduceti al treilea numar pentru media aritmetica: "))
media_aritmetica = (m + n + o) / 3
print("Media aritmetica a numerelor este: ", media_aritmetica)
print("Urmatorul exercitiu va incepe in: ")
print(3)
time.sleep(2)
print(2)
time.sleep(2)
print(1)
time.sleep(2)

# se introduc 3 numere la alegere apoi calculatorul va afisa media lor armonica
a = int(input("Introduceti primul numar pentru media armonica: "))
b = int(input("Introduceti al doilea numar pentru media armonica: "))
c = int(input("Introduceti al treilea numar pentru media armonica: "))
media_armonica = 3 / (1 / a + 1 / b + 1 / c)
print("Media armonica este: ", media_armonica)
print("Urmatorul exercitiu va incepe in: ")
print(3)
time.sleep(2)
print(2)
time.sleep(2)
print(1)
time.sleep(2)

# introduceti un numar din care se va scadea 3, adauga 43, inmultiti cu 3, si impariti cu 4.
numar = int(input("Introduceti un numar: "))
print("Noi scadem 3, adaugam 43, inmultim cu 3 si impartim la 4")
time.sleep(2)
rezultat = (numar - 3 + 43) * 3 / 4
print("Rezultatul este: ", rezultat)
# SAU
# a=5
# a=a-3
# a=a+43
# a=a*3
# a=a/4
# print(a)
print("Urmatorul exercitiu va incepe in: ")
print(3)
time.sleep(2)
print(2)
time.sleep(2)
print(1)
time.sleep(2)

# se calculeaza si afisaza pretul fara tva
pret_intreg = int(input("Introduceti un pret intreg(tva inclus): "))
tva = pret_intreg * 19 / 119
pret_fara_tva = pret_intreg - tva
print("Pretul fara tva este: ", pret_fara_tva)
print("Urmatorul exercitiu va incepe in: ")
print(3)
time.sleep(2)
print(2)
time.sleep(2)
print(1)
time.sleep(2)

# se afisaza aria cercului
raza_cercului = int(input("Introduceti o valoare pentru raza cercului: "))
pi = 3.14
aria_cercului = pi * raza_cercului ** 2
print("Aria cercului este: ", aria_cercului)
print("Urmatorul exercitiu va incepe in: ")
print(3)
time.sleep(2)
print(2)
time.sleep(2)
print(1)
time.sleep(2)

# echivalenta C in F
c = int(input("Introdu cate grade Celsius vrei:"))
f = (9 / 5 * c) + 32
k = c + 273.15
print("Echivalenta in F pentru valoarea introdusa este: ", f)
print("Echivalenta in K pentru valoarea introdusa este: ", k)
print("Urmatorul exercitiu va incepe in: ")
print(3)
time.sleep(2)
print(2)
time.sleep(2)
print(1)
time.sleep(2)

# verificare numere Pitagoreice
s = int(input("Introduceti o cateta: "))
r = int(input("Introduceti cealalta cateta: "))
p = int(input("Introduceti ipotenuza: "))
if p >= s + r:
    print("Ati introdus o ipotenuza prea mare!!!")
    time.sleep(3)
else:
    print("Ati introdus valori corecte :)")
    time.sleep(2)

stanga = s ** 2 + r ** 2
dreapta = p ** 2
if stanga == dreapta:
    print("Numerele sunt pitagoreice")
else:
    print("Numerele nu sunt pitagoreice")
time.sleep(2)
print("Urmatorul exercitiu va incepe in: ")
print(3)
time.sleep(2)
print(2)
time.sleep(2)
print(1)
time.sleep(2)

# volumul unui con
print("Introduceti elementele unui trunchi de con:")
rr = int(input("Introduceti raza mare: "))
r = int(input("Introduceti raza mica: "))
if rr <= r:
    print("Raza mica este mai mare sau egala cu raza mare!!!")
h = int(input("Introduceti inaltimea: "))
generatoarea_la_patrat = h ** 2 + (rr - r) ** 2
generatoarea = generatoarea_la_patrat ** 1 / 2
aria_laterala = 3.14 * generatoarea * (rr + r)
arie_baza_mare = 3.14 * rr ** 2
arie_baza_mica = 3.14 * r ** 2
volumul_trunchiului_de_con = (3.14 * h) * (rr ** 2 + r ** 2 + rr * r) / 3
print("Aria laterala a trunchiului de con este: ", aria_laterala)
time.sleep(2)
print("Aria bazei mari a trunchiului de con este: ", arie_baza_mare)
time.sleep(2)
print("Aria bazei mici a trunchiului de con este: ", arie_baza_mica)
time.sleep(2)
print("Volumul trunchiu de con pentru valorile date este: ", volumul_trunchiului_de_con)
