import turtle
import random

# Initialize the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
colors = ['red', 'green', 'blue', 'yellow']
turtle_speed = 1

# Function to draw the finishing line
def draw_finishing_line():
    line = turtle.Turtle()
    line.penup()
    line.goto(360, 300)
    line.right(90)
    line.pendown()
    line.forward(600)

# Function to generate turtles
def generate_turtles():
    turtles = []
    start_y = -100
    for color in colors:
        turtle_instance = turtle.Turtle(shape="turtle")
        turtle_instance.penup()
        turtle_instance.color(color)
        turtle_instance.goto(-360, start_y)
        turtles.append(turtle_instance)
        start_y += 60
    return turtles

# Main race function
def race():
    turtles = generate_turtles()
    bet = screen.textinput(title='Your bet', prompt="What's your bet? ")
    if bet not in colors:
        return

    is_race_on = True
    while is_race_on:
        for turtle_instance in turtles:
            if turtle_instance.xcor() > 360:
                is_race_on = False
                if turtle_instance.pencolor() == bet:
                    print(f"You've won! The {turtle_instance.pencolor()} turtle is the winner!")
                else:
                    print(f"You've lost. The {turtle_instance.pencolor()} turtle won.")
            rand_distance = random.randint(1, 10)
            turtle_instance.forward(rand_distance)

# Draw the finishing line
draw_finishing_line()

# Start the race
race()

# Close the window on click
screen.exitonclick()
