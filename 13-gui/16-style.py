from tkinter import Tk
from tkinter.ttk import Style, Button, Label, Entry

def change_style():
    style = Style()
    style.configure("TButton", foreground="red")
    style.configure("TLabel", foreground="blue", font=("Arial", 20))

def reset_style():
    style = Style()
    style.configure("TButton", foreground="black")
    style.configure("TLabel", foreground="black", font=("Arial", 16))

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

style = Style()
style.configure("TLabel", foreground="black", font=("Arial", 16))
style.configure("TEntry", foreground="red")

root.mainloop()