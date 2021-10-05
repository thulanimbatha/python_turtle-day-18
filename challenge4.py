from turtle import Turtle, Screen
import random

directions = [0, 90, 180, 270, 360]
colours = ["red", "blue", "green", "pink", "yellow", "purple", "orangered2", "skyblue"]

tmnt = Turtle()
tmnt.shape("turtle")
tmnt.pensize(13)
tmnt.speed("fastest")

for _ in range(100):
    tmnt.pencolor(random.choice(colours))
    tmnt.forward(40)
    tmnt.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()