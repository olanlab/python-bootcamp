import turtle
import tkinter as tk

def on_canvas_click(x, y):
    t.goto(x - 200, (y - 200) * -1)

def on_pen_color_change(color):
    t.pencolor(color)

def on_clear_button_click():
    t.clear()

def on_move_up_button_click():
    t.setheading(90)
    t.forward(10)

def on_move_down_button_click():
    t.setheading(270)
    t.forward(10)

def on_move_left_button_click():
    t.setheading(180)
    t.forward(10)

def on_move_right_button_click():
    t.setheading(0)
    t.forward(10)

win = tk.Tk()
win.title("Paint Program")

canvas = tk.Canvas(win, width=400, height=400)
canvas.pack()

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")
screen.delay(0)

t = turtle.RawTurtle(screen)
t.pensize(5)

canvas.bind("<Button-1>", lambda event: on_canvas_click(event.x, event.y))

pen_color_label = tk.Label(win, text="Pen color:")
pen_color_label.pack(side="left")

pen_color_var = tk.StringVar()
pen_color_var.set("black")
pen_color_menu = tk.OptionMenu(win, pen_color_var, "black", "red", "green", "blue", command=on_pen_color_change)
pen_color_menu.pack(side="left")

clear_button = tk.Button(win, text="Clear", command=on_clear_button_click)
clear_button.pack(side="left")

move_up_button = tk.Button(win, text="Up", command=on_move_up_button_click)
move_up_button.pack()

move_left_button = tk.Button(win, text="Left", command=on_move_left_button_click)
move_left_button.pack(side="left")

move_right_button = tk.Button(win, text="Right", command=on_move_right_button_click)
move_right_button.pack(side="left")

move_down_button = tk.Button(win, text="Down", command=on_move_down_button_click)
move_down_button.pack()



win.mainloop()
