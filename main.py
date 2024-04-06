from tkinter import *

window = Tk()

window.minsize(width=400,height=400)
window.title("Hello World")

label = Label(text="Hello world")
label.pack()


def got_clicked():
    label.config(text=input.get())


button = Button(text="Click me", command=got_clicked)
button.pack()

input = Entry(width=10)
input.pack()

window.mainloop()