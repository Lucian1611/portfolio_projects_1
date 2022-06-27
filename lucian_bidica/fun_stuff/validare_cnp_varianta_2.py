
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