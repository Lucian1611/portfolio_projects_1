def celsius_to_farenheight(celsius):
    try:
        farenheight = 9 / 5 * float(celsius) + 32
        return round(farenheight, 2)
    except TypeError:
        print("Va rugam introduceti o valoare valida!: ")

# celsius= float(input("Introduceti o valoare: "))
# print(celsius_to_farenheight())
