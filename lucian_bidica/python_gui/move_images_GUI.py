from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-3)
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+3)
def move_left(event):
    label.place(x=label.winfo_x()-3, y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+3, y=label.winfo_y())

window = Tk()
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<d>", move_right)
window.bind("<a>", move_left)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)
window.bind("<Left>", move_left)

window.geometry("500x500")
myimage = PhotoImage(file="3.png")
label = Label(window, image=myimage)
label.place(x=0, y=0)

window.mainloop()