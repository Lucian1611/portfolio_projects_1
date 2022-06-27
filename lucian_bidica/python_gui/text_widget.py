from tkinter import *


def trimitere():
    input = text.get("1.0", END)
    print(input)


window = Tk()
text = Text(window,
            bg="light blue",
            font=("Ink Free", 20),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg = "dark green")
text.pack()
button = Button(window, text="trimite", command=trimitere)
button.pack()
window.mainloop()
