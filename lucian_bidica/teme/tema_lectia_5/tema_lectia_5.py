import time


# 1. Sa se scrie o clasa Brad, cu proprietatie: baza, ..., si metodele __init__, __str__
class Brad:
    def __init__(self, baza):
        self.baza = baza

    def juma_de_brad(self):
        for i in range(1, baza):
            print("#" * i)
            i = i + 1

    def un_brad_frumos(self):
        j = 1
        k = baza // 2
        while j <= baza:
            print("  " * k, "#" * j, " " * k)
            j += 2
            k -= 1

    def un_brad_cu_nori(self):
        j = 1
        k = baza // 2
        while j <= baza:
            print(" ^" * k, "#" * j, " ^" * k)
            j += 2
            k -= 1


baza = int(input("Introduceti baza bradului: "))
brad1 = Brad(baza)
brad1.juma_de_brad()
print()
brad1.un_brad_frumos()
print()
brad1.un_brad_cu_nori()
print()
time.sleep(2)


# 2. Folosind functii recursive, sa se afle daca un numar este palindrom.
def palindrom(variabila):
    if len(variabila) < 1:
        return True
    else:
        if variabila[0] == variabila[-1]:
            return palindrom(variabila[1:-1])
        else:
            return False


var = input("""Introduceti un sir caractere pentru a verifica 
        daca este palindrom: """)
if palindrom(var) == True:
    print("String-ul este Palindrom!")
else:
    print("String-ul NU ESTE palindrom!")
time.sleep(2)


# 3. Sa se scrie o clasa TemperatureConverter, cu metodele:
#     - celsius_to_fahrenheit_and_kelvin
#     - fahrenheit_to_celsius_and_kelvin
#     - kelvin_to_celsius_and_fahrengheit
# (am restrans un pic numarul de metode sa ruleze mai elegant si folositor pentru utilizator)

class ConvertorTemperatura:
    def __init__(self, valoare):
        self.valoare = valoare

    def c_to_f_and_k(self):
        f = 9 / 5 * valoare + 32
        k = valoare + 273
        return print(f"""Temperatura de {valoare} grade Celsius este egala cu 
    {f} grade Fahrenheit sau {k} grade Kelvin""")

    def f_to_c_and_k(self):
        c = 5 / 9 * (valoare - 32)
        k = 5 / 9 * (valoare - 32) + 273
        return print(f"""Temperatura de {valoare} grade Fahrenheit este egala cu 
            {c} grade Celsius sau {k} grade Kelvin""")

    def k_to_c_and_f(self):
        f = 9 / 5 * (valoare - 273) + 32
        c = valoare - 273
        return print(f"""Temperatura de {valoare} grade Kelvin este egala cu 
                {c} grade Celsius sau {f} grade Fahrenheit""")


valoare = float(input("Introduceti o valoare a temperaturii: "))
u_d_m = input("""Introduceti unitatea de masura din care vreti sa convertiti:
C pentru celsius
F pentru Fahrenheit
K pentru Kelvin""").upper()
transformare1 = ConvertorTemperatura(valoare)
if u_d_m == "C":
    transformare1.c_to_f_and_k()
elif u_d_m == "F":
    transformare1.f_to_c_and_k()
elif u_d_m == "K":
    transformare1.k_to_c_and_f()
else:
    print("Ati introdus o litera gresita!!!")
time.sleep(2)


# 4. Sa se scrie o clasa CosCumparaturi cu:
#     - produse (lista)
#     - user (User)
#     - status (str)
#     - metoda __init__
#     - metoda __str__
#     - metoda __len__, care returneaza lungimea listei cu produse
class ListaCumparaturi:
    def __init__(self, produse, user, status):
        self.produse = produse
        self.user = user
        self.status = status

    def __str__(self):
        return (f"Produsele din cos: {self.produse}")

    def __len__(self):
        return len(self.produse)


produse = ["ceapa", "ardei", "morcovi", "usturoi", "mere"]
user = "Lucian Bidica"
status = "online"
cosul1 = ListaCumparaturi(produse, user, status)
print(cosul1)
print(len(cosul1))
