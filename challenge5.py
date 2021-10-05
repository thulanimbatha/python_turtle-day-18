# drawing a Spinograph
import turtle as T
import random

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tmnt = T.Turtle()
tmnt.shape("turtle")
tmnt.speed("fastest")
T.colormode(255)
# we want turtle to make 360 deg turn then stop -> range = 360 / angle_tilt -> 72 = 360 / 5
for _ in range(72):
    tmnt.color(random_colour())
    tmnt.circle(100)
    tmnt.setheading(tmnt.heading() + 5)

screen = T.Screen()
screen.exitonclick()