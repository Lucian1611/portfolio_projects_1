#Rezolvare Tema Lectia 1 - Suplimentara
"""Exercitiul 1
se alege o unitate de masura pentru a fi convertita
si o unitate de masura pentru a face conversia"""
import time

temp_initiala = input("""Alegeti unitatea de masura din care vreti sa convertiti:
                                a: Celsius
                                b: Fahrenheight
                                c: Kelvin:
                                Introduceti litera corespunzatoare (Tastati a, b sau c): """).lower()
optiuni = ["a", "b", "c"]
while temp_initiala not in optiuni:
    print("Va rugam alegeti o optiune valida!!!")
    print()
    time.sleep(1.2)
    temp_initiala = input("""Alegeti unitatea de masura din care vreti sa convertiti:
                                    a: Celsius
                                    b: Fahrenheight
                                    c: Kelvin:
                                    Introduceti litera corespunzatoare (Tastati a, b sau c): """).lower()
temp_convertita = input("""Alegeti unitatea de masura in care vreti sa convertiti:
                                a: Celsius
                                b: Fahrenheight
                                c: Kelvin:
                                Introduceti litera corespunzatoare (Tastati a, b sau c): """).lower()
while temp_convertita not in optiuni:
    print("Va rugam alegeti o optiune valida!!!")
    print()
    time.sleep(1.2)
    temp_convertita = input("""Alegeti unitatea de masura in care vreti sa convertiti:
                                    a: Celsius
                                    b: Fahrenheight
                                    c: Kelvin:
                                    Introduceti litera corespunzatoare (Tastati a, b sau c): """).lower()
valoare1 = int(input("Introduceti valoarea temperaturii pe care vreti sa o convertiti: "))
if temp_initiala == "a" and temp_convertita == "b":
    valoare2 = 9 / 5 * valoare1 + 32
    print(valoare1, " Celsius=", valoare2, " Fahrengheit")
elif temp_initiala == "a" and temp_convertita == "c":
    valoare3 = valoare1 + 273
    print(valoare1, " Celsius=", valoare3, " Kelvin")
elif temp_initiala == "b" and temp_convertita == "a":
    valoare4 = 5 / 9 * (valoare1 - 32)
    print(valoare1, " Fahrengheit=", valoare4, " Celsius")
elif temp_initiala == "b" and temp_convertita == "c":
    valoare5 = 5 / 9 * (valoare1 - 32) + 273
    print(valoare1, " Fahrenheight=", valoare5, " Kelvin")
elif temp_initiala == "c" and temp_convertita == "a":
    valoare6 = valoare1 - 273
    print(valoare1, " Kelvin=", valoare6, " Celsius")
elif temp_initiala == "c" and temp_convertita == "b":
    valoare7 = 9 / 5 * (valoare1 - 273) + 32
    print(valoare1, " Kelvin= ", valoare7, " Fahrengheit")
else:
    print("Ati introdus litere gresite!!!")
print()
print("Asteptati... urmeaza exercitiul 2...")
time.sleep(3)

# Exercitiul 2
# timp in secunde transformat in ore/minute/secunde
timp = int(input("Introduceti un numar de secunde: "))
zile = timp // 86400
ore = (timp - (zile * 86400)) // 3600
minute = (timp - (zile * 86400) - (ore * 3600)) // 60
secunde = timp - (zile * 86400) - (ore * 3600) - (minute * 60)
print(timp, " secunde = ", zile, "zile,", ore, "ore ", minute, " minute ", secunde, " secunde ")
print()
print("Asteptati... urmeaza exercitiul 3...")
time.sleep(3)

# Exercitiul 3
""" Vom calcula profitul dupa vanzare pentru produse cumparate la un pret (fara TVA), 
introdus de utilizator si vandute la un alt pret"""
pret_achizitie = int(input("Introduceti pretul de achizitie fara TVA(in lei): "))
pret_produs = pret_achizitie + 0.19 * pret_achizitie
pret_vanzare = int(input("Introduceti pretul de vanzare(in lei): "))
numar_produse_vandute = int(input("Introduceti numarul de produse vandute: "))
profit = (pret_vanzare * numar_produse_vandute) - (pret_produs * numar_produse_vandute)
if pret_vanzare < pret_produs:
    print("Ati iesit in pierdere!!!")
else:
    print("Super!!! Ati facut ceva profit :)")
print("Pentru ", numar_produse_vandute, "produse vandute profitul dumneavoastra este: ", profit, "lei")
