from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[("Fisier text", ".txt"),
                                               ("Fisier HTML", ".html"),
                                               ("Fisier pdf", ".pdf"),
                                               ("Toate fisierele", ".")])
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text = "save", command = saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()

