import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create a rectangle on the canvas
rect = canvas.create_rectangle(50, 50, 150, 150, fill="blue")

# Create a line on the canvas
line = canvas.create_line(0, 0, 300, 300, fill="red")

root.mainloop()