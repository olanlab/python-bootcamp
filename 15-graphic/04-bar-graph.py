import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(600, 600)

# Create the turtle object
t = turtle.Turtle()

# Define the data for the bar graph
data = [50, 75, 100, 85, 60]

# Set the size of the bar graph
bar_width = 50
bar_height = 200

# Set the starting position for the turtle
x_start = -200
y_start = -200

# Draw the bars
for i in range(len(data)):
    # Move the turtle to the correct starting position
    t.penup()
    t.goto(x_start + i * bar_width, y_start)
    t.pendown()
    
    # Draw the bar
    t.begin_fill()
    t.color("blue")
    t.setheading(90)
    t.forward(data[i]/100 * bar_height)
    t.right(90)
    t.forward(bar_width)
    t.right(90)
    t.forward(data[i]/100 * bar_height)
    t.end_fill()

# Exit on click
screen.exitonclick()