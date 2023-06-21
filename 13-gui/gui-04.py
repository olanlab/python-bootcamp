import tkinter as tk

root = tk.Tk()
root.configure(width=300, height=350)

label1 = tk.Label(root, text="Label 1", width=10, height=5, bg="red", fg="white")
label1.place(x=50, y=50)

label2 = tk.Label(root, text="Label 2", width=10, height=5, bg="green", fg="white")
label2.place(x=150, y=50)

label3 = tk.Label(root, text="Label 3", width=10, height=5, bg="blue", fg="white")
label3.place(x=100, y=150)

button = tk.Button(root, text="Click me!", width=10, height=2, bg="yellow", fg="black")
button.place(x=75, y=250)

root.mainloop()
