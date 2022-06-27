from tkinter import *


def printeaza():
    print(inserare_nume, inserare_prenume, inserare_adresa_email)


window = Tk()

nume = Label(window, text="Numele: ").grid(row=0, column=0)
inserare_nume = Entry(window).grid(row=0, column=1)

prenumele = Label(window, text="Prenumele: ").grid(row=1, column=0)
inserare_prenume = Entry(window).grid(row=1, column=1)

adresa_email = Label(window, text="Email:  ").grid(row=2, column=0)
inserare_adresa_email = Entry(window).grid(row=2, column=1)

submit_button = Button(window, text="Submit", command=printeaza).grid(row=3, column=0, columnspan=2)

window.mainloop()
