from tkinter import *


def functie_cont_lei():
    print("""Sold cont: 200 RON
                Nu exista tranzactii pe luna in curs""")


def functie_cont_euro():
    print("""Sold cont: 5000 Euro
                  Nu exista tranzactii pe luna in curs""")


def functie_informatii_cont():
    print("Acestea sunt informatiile despre profilul/contul dumneavoastra: ")


def functie_gestionare_carduri():
    print(""""Aici puteti gestiona cardurile dumneavoastra:
    VISA 1234 5678 9900 1111
    MasterCard 3344 5566 7788 9900""")


def functie_setari_cont():
    print("Aici se fac setarile contului")


window = Tk()
meniu = Menu(window)
window.config(menu=meniu)
fileMenu = Menu(meniu, tearoff=0, font=("Times New Roman", 20))
meniu.add_cascade(label="conturi", menu=fileMenu)
fileMenu.add_command(label="RO51BTRLEU0001", command=functie_cont_lei)
fileMenu.add_command(label="RO51BTRLEUR001", command=functie_cont_euro)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(meniu, tearoff=0, font=("Times New Roman", 20))
meniu.add_cascade(label="profilul meu", menu=editMenu)
editMenu.add_command(label="Informatii Utilizator", command=functie_informatii_cont)
editMenu.add_command(label="Gestionare Carduri", command=functie_gestionare_carduri)
editMenu.add_command(label="Setari", command=functie_setari_cont)
editMenu.add_separator()
editMenu.add_command(label="Exit", command=quit)

window.mainloop()
