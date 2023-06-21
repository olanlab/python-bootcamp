import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1", width=10, height=5, bg="red", fg="white")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="Label 2", width=10, height=5, bg="green", fg="white")
label2.grid(row=0, column=1, padx=10, pady=10)

label3 = tk.Label(root, text="Label 3", width=10, height=5, bg="blue", fg="white")
label3.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

button = tk.Button(root, text="Click me!", width=10, height=2, bg="yellow", fg="black")
button.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="we")

root.mainloop()
