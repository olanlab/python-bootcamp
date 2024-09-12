import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1", width=10, height=5, bg="red", fg="white")
label1.pack(side="left", padx=10, pady=10, fill="y")

label2 = tk.Label(root, text="Label 2", width=10, height=5, bg="green", fg="white")
label2.pack(side="left", padx=10, pady=10, fill="y")

label3 = tk.Label(root, text="Label 3", width=10, height=5, bg="blue", fg="white")
label3.pack(side="left", padx=10, pady=10, fill="y")

button = tk.Button(root, text="Click me!", width=10, height=2, bg="yellow", fg="black")
button.pack(side="top", padx=10, pady=10, fill="x")

root.mainloop()
