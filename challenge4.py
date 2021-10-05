import turtle 
import random

directions = [0, 90, 180, 270, 360]

tmnt = turtle.Turtle()
tmnt.shape("turtle")
tmnt.pensize(13)
tmnt.speed("fastest")
turtle.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(100):
    tmnt.pencolor(random_colour())
    tmnt.forward(40)
    tmnt.setheading(random.choice(directions))

screen = turtle.Screen()
screen.exitonclick()