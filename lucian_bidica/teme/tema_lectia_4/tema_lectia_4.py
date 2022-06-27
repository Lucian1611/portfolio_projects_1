# Rezolvare Tema Lectia 4
import time


# 1. Conversia unei temperaturi din 'C in 'F:
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


temperatura = float(input("Temperatura in grade C este: "))
print("Temperatura convertita in grade F este: ", celsius_to_fahrenheit(temperatura))
print()
print("-----------------------------Exercitiul 2 -----------------------------")
time.sleep(2)


# 2. Conversia unei temperaturi din 'F in 'C
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


temperatura = float(input("Temperatura in grade F este: "))
print("Temperatura convertita in grade C este: ", fahrenheit_to_celsius(temperatura))
print()
print("-----------------------------Exercitiul 3 -----------------------------")
time.sleep(2)


# 3. Produsul tuturor numerelor de la 1 pana la o valoare primita ca parametru
def produs(valoare):
    produsul = 1
    for i in range(1, valoare + 1):
        produsul = produsul * i
    return produsul


valoare = int(input("Introduceti o valoare pentru a afla produsul: "))
print("Produsul tuturor numerelor pana la valoarea introdusa este : ", produs(valoare))
print()
print("-----------------------------Exercitiul 4 -----------------------------")
time.sleep(2)


# 4. Media armonica a oricator valori primite prin parametru
def media_armonica(*args):
    numarator = len(args)
    numitor = 0
    for i in args:
        numitor += 1 / i
    return numarator / numitor


print("Media armonica este: ", media_armonica(3, 8))
print()
print("-----------------------------Exercitiul 5 -----------------------------")
time.sleep(2)

# 5. Calculul ariei unui cerc, cu raza primita prin parametru
import math


def aria(raza):
    aria_cercului = math.pi * (raza ** 2)
    return aria_cercului


raza = int(input("Introduceti raza cercului: "))
print("Aria cercului este: ", aria(raza))
print()
print("-----------------------------Exercitiul 6 -----------------------------")
time.sleep(2)


# 6. Calculul volumului unei sfere cu raza primita prin parametru
def volum(raza):
    volumul = (4 * math.pi * (raza ** 3)) / 3
    return volumul


raza = int(input("Introduceti raza sferei: "))
print("Volumul sferei este: ", volum(raza))
print()
print("-----------------------------Exercitiul 7 -----------------------------")
time.sleep(2)


# 7. Afisarea brazilor din tema de data trecuta, cu valori date ca parametri de intrare obligatorii si/sau optionali.
def bradut(baza, frunza="#", cer=" ", nor="^"):
    spatiu = baza // 2
    for index in range(1, baza + 1, 2):
        if spatiu > 1:
            print(nor * (spatiu - 1) + cer, end="")
        elif spatiu == 1:
            print(cer, end="")
        print(frunza * index, end="")
        if spatiu > 1:
            print(cer + nor * (spatiu - 1), end="")
        elif spatiu == 1:
            print(cer, end="")
        spatiu -= 1
        print()


bradut(25, nor="~")
print()
print("-----------------------------Exercitiul 8 -----------------------------")
time.sleep(2)


# 8. Conversia unui string de forma "1.234.567,89 Lei" la un float de forma 1234567.89
def conversie(numar):
    numar_float = numar.replace(".", "")
    numar_float = numar_float.replace(",", ".")
    numar_float = float(numar_float)
    return numar_float


numar = input("Introduceti un numar cu mai multe puncte si o virgula: ")
print(conversie(numar))
print()
print("-----------------------------Exercitiul 9 -----------------------------")
time.sleep(2)


# 9. Numararea aparitiilor fiecarui caracter dintr-un string primit ca parametru. Rezultatul sa fie un dictionar cu forma
#    {"a":1, "b":3, ...}
def numarare_caractere(lista):
    dictionar = {}
    for i in lista:
        count = lista.count(i)
        dictionar.update({i: count})
    return dictionar


lista = ["a", "a", "b", "b", "b", "c", "c", "c", "c", "d"]
print(numarare_caractere(lista))
print()
print("-----------------------------Exercitiul 10 -----------------------------")
time.sleep(2)


# 10. Generarea unui drepunghi in terminal cu latimea si lungimea date ca parametri.
# Aici am facut sa printeze un dreptunghi plin, alcatuit dintr-un simbol dat
def dreptunghi(coloane, randuri, symbol):
    for i in range(coloane):
        for j in range(randuri):
            print(symbol, end="")
        print()


coloane = int(input("Introduceti numarul de coloane: "))
randuri = int(input("Introduceti numarul de randuri:"))
symbol = input("Introduceti simbolul pe care doriti sa il folositi:")
dreptunghi(coloane, randuri, symbol)

print()
print("-----------------------------SAU -----------------------------")
time.sleep(2)
picture = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
for i in picture:
    print()
    for j in i:
        if j == 0:
            print("  ", end="")
        else:
            print("o", end="")
print()
print("-----------------------------Exercitiul 11 -----------------------------")
time.sleep(2)


# 11. Reducerea preciziei unui float primit ca parametru la 2 zecimale
def reducere_la_doua_zecimale(nr):
    print(round(nr, 2))


nr = float(input("Introduceti un numar cu muuulllllteeee zecimale: "))
reducere_la_doua_zecimale(nr)


# 12. Generarea unui cerc in terminal, cu raza data de la tastatura.
# Nu am idee

# 13. Sa se calculeze produsul tuturor numerelor pana la o valore data ca parametru. Sa se implementeze recursiv.
def functie_produs(valoare):
    if valoare <= 1:
        return 1
    else:
        return valoare * functie_produs(valoare - 1)


valoare = int(input("Introduceti un numar pana la care sa calculam produsul: "))
print(functie_produs(valoare))
