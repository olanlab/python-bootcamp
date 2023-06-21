from turtle import Turtle, colormode, Screen
import random

colormode(255)  
t = Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# CODE 3
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_side_n in range(3, 10):
    t.color(random_color())
    draw_shape(shape_side_n)

# CODE 4
t.penup()
t.goto(x=50, y=210)
t.pendown()
t.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

draw_spirograph(10) 

s = Screen()
s.exitonclick()