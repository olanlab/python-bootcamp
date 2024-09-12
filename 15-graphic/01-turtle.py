from turtle import Turtle, colormode, Screen, setup

colormode(255)  
setup(width=800, height=600, startx=0, starty=0)
t = Turtle()

# CODE 1
t.shape("turtle")
t.color((255, 204, 255 ))
t.hideturtle()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)


# CODE 2
for _ in range(15) : 
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


s = Screen()
s.exitonclick()