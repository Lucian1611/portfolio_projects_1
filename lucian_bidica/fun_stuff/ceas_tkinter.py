from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%d  %B   %Y")
    date_label.config(text=date_string)

    time_label.after(1000, update)  # 1000 milisecunde (o secunda)
    # update este functie recursiva
    # window.after(1000, update)   <<< merge si cu window.after


window = Tk()

time_label = Label(window, font=("Times New Roman", 80), fg="yellow", bg="dark grey")
time_label.pack()

day_label = Label(window, font=("Times New Roman", 50), fg="red")
day_label.pack()

date_label = Label(window, font=("Times New Roman", 50), fg="green")
date_label.pack()

update()

window.mainloop()
