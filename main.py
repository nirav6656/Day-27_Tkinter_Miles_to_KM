from tkinter import *
from tkinter.ttk import *

window = Tk()

# window.minsize(width=400,height=600)
# window.title("Hello World")
#
# label = Label(text="Hello world")
# label.pack()
#
#
# def got_clicked():
#     label.config(text=input.get())
#
#
# button = Button(text="Click me", command=got_clicked)
# button.pack()
#
# input = Entry(width=10)
# input.pack()
#
# large_box = Text(width=20,height=10)
# large_box.focus()
# large_box.pack()
# print(large_box.get("1.0", END))
# large_box.pack()
#
# # Spinbox
# spinbox = Spinbox(from_=0,to=5)
# spinbox.pack()
#
# # Scale
# scale = Scale(from_=0, to=10)
# scale.pack()
#
#
# def onclick():
#
#     print(chekedstate.get())
#
# chekedstate = IntVar()
# checkbutton = Checkbutton(text="Is on",variable=chekedstate,command=onclick)
# checkbutton.pack()
#
# # Radiobutton
# def onclick():
#     print(clicked_state.get())
# clicked_state = IntVar()
#
# radiobutton1 = Radiobutton(text="Option 1",value=1,variable=clicked_state,command=onclick)
# radiobutton2 = Radiobutton(text="Option 2",value=2,variable=clicked_state,command=onclick)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
#
# # Listbox
# listbox = Listbox(height=5)
#
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.pack()

# Started new project Miles to KM
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

window.title("Miles to KM Converter")

# Box lable

# get_miles = IntVar()
box_label = Entry(width=30)
# box_label.insert(END, string="Some text")

box_label.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# is equal to label
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

# Answer in KM label

answer = Label(text="0")
answer.grid(column=1, row=1)

# KM label
km = Label(text="KM")
km.grid(column=2, row=1)


# Calculate Button
# get_miles =
# print(get_miles)



def onclick():
    print(box_label.get())
    answer_in_km = float(box_label.get()) * 1.60934
    answer.config(text=answer_in_km)


button = Button(text="Calculate", command=onclick)
button.grid(column=1, row=2)

window.mainloop()
