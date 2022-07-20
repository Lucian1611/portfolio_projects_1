from tkinter import *


def move_up(event):
    canvas.move(myimage, 0, -10)


def move_down(event):
    canvas.move(myimage, 0, 10)


def move_left(event):
    canvas.move(myimage, -10, 0)


def move_rigth(event):
    canvas.move(myimage, 10, 0)


window = Tk()

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_rigth)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Right>", move_rigth)
window.bind("<Left>", move_left)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

background_photo = PhotoImage(file="yellow_background.png")
other_image = canvas.create_image(0, 0, image=background_photo, anchor=NW)

photoimage = PhotoImage(file="3.png")
myimage = canvas.create_image(0, 0, image=photoimage, anchor=NW)

window.mainloop()
