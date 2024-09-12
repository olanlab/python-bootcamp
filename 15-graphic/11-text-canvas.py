import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create two text items on the canvas with different fonts and colors
canvas.create_text(100, 100, text="Hello", font=("Arial", 16), fill="red")
canvas.create_text(200, 200, text="World", font=("Times", 24), fill="blue")

root.mainloop()
