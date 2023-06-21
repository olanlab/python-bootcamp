import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Define gradient colors
colors = ["#FF0000", "#FFFF00", "#00FF00", "#00FFFF", "#0000FF", "#FF00FF"]

# Create a rectangle with a gradient fill
for i in range(len(colors)):
    x1 = 0
    y1 = i * (300 // len(colors))
    x2 = 300
    y2 = (i + 1) * (300 // len(colors))
    canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i], outline="")

root.mainloop()