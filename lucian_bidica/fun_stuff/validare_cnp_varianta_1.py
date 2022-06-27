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
