from tkinter import *


def create_window():
    next_window = Toplevel()


window = Tk()
Button(window, text="create new window", command=create_window).pack()

window.mainloop()
