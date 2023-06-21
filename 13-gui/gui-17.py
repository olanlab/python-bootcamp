from tkinter import Tk
from tkinter.ttk import Style, Button, Label, Entry

def change_style():
    style = Style()
    style.theme_use("classic")

def reset_style():
    style = Style()
    style.theme_use("aqua")


root = Tk()
root.geometry("200x200")
label1 = Label(root, text="Hello World")
label1.pack()

label2 = Label(root, text="Python Language")
label2.pack()

button1 = Button(root, text="Change Style", command=change_style)
button1.pack()

button2 = Button(root, text="Reset", command=reset_style)
button2.pack()

entry1 = Entry(root, width=10)
entry1.pack()

entry2 = Entry(root, width=10)
entry2.pack()

root.mainloop()