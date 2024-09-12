


import turtle
import tkinter as tk

win = tk.Tk()
win.title("Turtle Example")

canvas = tk.Canvas(win, width=400, height=400)
canvas.pack()

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)

button = tk.Button(win, text="Quit", command=win.destroy)
button.pack()

for i in range(4):
    t.forward(50)
    t.left(90)

win.mainloop()
