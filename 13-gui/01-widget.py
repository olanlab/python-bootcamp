from tkinter import *

# Window
window = Tk()
window.title("Window")
window.minsize(width=500, height=500)

# Menus
menubar = Menu(window)
window.config(menu=menubar)
file_menu = Menu(menubar)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=window.destroy)
menubar.add_cascade(label="File", menu=file_menu)

# Labels
label = Label(text="Label")
label.pack()

# Entry
entry = Entry(width=30)
entry.insert(END, string="Entry")
entry.pack()
print(entry.get())

# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Text")
print(text.get("1.0", END))
text.pack()

# Buttons
def action():
    print("Action - On Click Button")
button = Button(text="Button", command=action)
button.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=50, width=20, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="Checkbox", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = StringVar()
radiobutton1 = Radiobutton(text="Radiobutton 1", value="All", variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Radiobutton 2", value="Male", variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Radiobutton 3", value="Female", variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=3)
lists = ["List 1", "List 2", "List 3", "List 4", "List 5"]
for item in lists:
    listbox.insert(lists.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

print("Hello world what is this!! what how to fix bug")

window.mainloop()