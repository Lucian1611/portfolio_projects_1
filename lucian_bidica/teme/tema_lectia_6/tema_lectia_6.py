# Sa se scrie o ierarhie de clase pentru o aplicatie bancara (de plata) specific de economisit bani.
# Clase sugerate: User, Payment. La fiecare Payment instantiat dintr-o valoare p1 = Payment(13.73),
# sa se rotunjeasca pana la prima valoare intreaga (14) , si sa se puna deoparte diferenta(0.27)
# Sa se scrie un test simplu pentru caz (edited)

# Specific pentru exercitiul meu: >>> Contul are un sold initial de 200 de lei, iar valoarea economisita pleaca de la 0
import math


class User:
    def __init__(self, nume, nr_cont):
        self.nume = nume
        self.nr_cont = nr_cont


class Payment(User):
    def __init__(self, nume, nr_cont, valoare_platita, total_cont, valoare_economisita):
        super().__init__(nume, nr_cont)
        self.valoare_platita = valoare_platita
        self.total_cont = total_cont
        self.valoare_economisita = valoare_economisita

    def plata(self):
        if valoare_platita > self.total_cont:
            print("Fonduri insuficiente")
        else:
            self.valoare_economisita += math.ceil(valoare_platita) - valoare_platita
            self.total_cont -= math.ceil(valoare_platita)
            if self.nume[-1] == "a":
                print(f"""Doamna {self.nume},
In contul {self.nr_cont} mai aveti disponibila suma de {self.total_cont} lei
Valoare economisita: {self.valoare_economisita}""")
            else:
                print(f"""Domnul {self.nume},
In contul {self.nr_cont} mai aveti disponibila suma de {self.total_cont} lei
Valoare economisita: {self.valoare_economisita}""")
            list_ = self.total_cont, self.valoare_economisita
            return list_


def read_float():
    while True:
        try:
            valoare_platita = float(input("Introduceti suma de plata: "))
            return valoare_platita
        except ValueError:
            print("Va rugam sa introduceti o valoare valida! ")
            continue


nume = input("Introduceti prenumele dumneavoastra : ")
nr_cont = input("Introduceti numarul de cont: ")
user1 = User(nume, nr_cont)
total_cont = 200
valoare_economisita = 0

valoare_platita = read_float()

p1 = Payment(user1.nume, user1.nr_cont, valoare_platita, total_cont, valoare_economisita)
total_cont, valoare_economisita = p1.plata()

# Se verifica daca se doreste o plata noua
optiune_plata = input("Doriti sa efectuati o noua plata? da/nu ")
while optiune_plata != "da" and optiune_plata != "nu":
    optiune_plata = input("Va rugam introduceti \"da  "  "sau \"nu\": ")
else:
    while optiune_plata == "da":
        # se face verificarea valorii introduse (nu este acceptata o valoare invalida)
        try:
            valoare_platita = float(input("Introduceti suma de plata: "))
            p1.plata()
        except ValueError:
            print("Ati introdus o valoare gresita!!!")

        optiune_plata = input("Doriti sa efectuati o noua plata? da/nu ")
