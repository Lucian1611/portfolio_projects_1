from tkinter import *
from ball_class import *
import time

window = Tk()
WIDTH = 600
HEIGHT = 600

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "red")
tenis_ball = Ball(canvas, 0, 0, 40, 4, 3, "green")
golf_ball = Ball(canvas, 0, 0, 22, 7, 5, "dark grey")

while True:
    volley_ball.move() 
    tenis_ball.move()
    golf_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
