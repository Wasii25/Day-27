from tkinter import Tk, Label, Button, Entry

def button_clicked():
    print("I got clicked")
    new = input.get()
    my_label.config(text=new)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=100, pady=200)

#Button
button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)

#new button
new_button = Button(text="Click Me!", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry
input = Entry()
input.grid(column=3, row=2)
print(input.get())

window.mainloop()
