# from tkinter import Tk, Label, Button, Entry
#
# def button_clicked():
#     print("I got clicked")
#     new = input.get()
#     my_label.config(text=new)
#
#
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)
#
# #Label
# my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.grid(column=0, row=0)
# my_label.config(padx=100, pady=200)
#
# #Button
# button = Button(text="Click Me!", command=button_clicked)
# button.grid(column=1, row=1)
#
# #new button
# new_button = Button(text="Click Me!", command=button_clicked)
# new_button.grid(column=2, row=0)
#
# #Entry
# input = Entry()
# input.grid(column=3, row=2)
# print(input.get())
#
# window.mainloop()
from tkinter import *

def converter():
    miles = float(miles_input.get())
    km = miles*1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to KM converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


is_equal_to = Label(text="Is equal to")
is_equal_to.grid(column=0, row=1)


kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)


kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)


calculate_button = Button(text="Calculate", command=converter)
miles_input.grid(column=1, row=2)

window.mainloop()
