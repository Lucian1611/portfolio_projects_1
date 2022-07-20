from tkinter import *

window = Tk()
frame= Frame(bg="purple", bd=5, relief=RAISED)
frame.place(x=20, y=30)

Button(frame, text="W", font= ("Consolas", 20), width=3).pack(side=TOP)
Button(frame, text="A", font= ("Consolas", 20), width=3).pack(side=LEFT)
Button(frame, text="S", font= ("Consolas", 20), width=3).pack(side=LEFT)
Button(frame, text="D", font= ("Consolas", 20), width=3).pack(side=LEFT)

window.mainloop()