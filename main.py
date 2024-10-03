from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    new = input.get()
    my_label.config(text=new)


button = Button(text="Click Me!", command=button_clicked)
button.pack()

input = Entry()
input.pack()
print(input.get())

window.mainloop()
