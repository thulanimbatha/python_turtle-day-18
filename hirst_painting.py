# Day 18 project
import turtle as t
import random

# turtle object
tmnt = t.Turtle()
# change colour mode so that we can use rgb colours
t.colormode(255)
# get colours from image -> from getColours.py
colour_list = [(252, 250, 235), (241, 252, 245), (253, 245, 249), (232, 243, 249), (238, 231, 79), (180, 16, 43), (219, 64, 99), (109, 179, 204), (185, 74, 38), (25, 122, 166), (186, 42, 67), (207, 152, 102), (22, 136, 85), (188, 176, 23), (20, 31, 68), (216, 130, 154), (70, 170, 100), (19, 166, 208), (232, 230, 6), (217, 78, 55), (38, 46, 112), (127, 184, 138), (8, 51, 33), (235, 165, 182), (149, 210, 220), (163, 24, 20), (10, 98, 55), (156, 213, 189), (237, 171, 163), (87, 21, 61), (6, 87, 107), (85, 12, 8), (115, 118, 151), (174, 184, 217), (248, 11, 27)]
tmnt.speed("fastest")

'''MOVE TURTLE TO THE BOTTOM LEFT WITHOUT PEN LINE'''
tmnt.setheading(230)
tmnt.penup()
tmnt.forward(350)
tmnt.setheading(0)

'''BEGIN LOOP: MAKE 10 x 10 GRID OF COLOUR DOTS'''
for _ in range(10):
    for _ in range(10):
        tmnt.dot(20, random.choice(colour_list))
        tmnt.forward(50)
    # reset turtle position
    tmnt.setheading(90)
    tmnt.forward(50)
    tmnt.setheading(180)
    tmnt.forward(500)
    tmnt.setheading(0)

screen = t.Screen()
screen.exitonclick()
