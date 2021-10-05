from turtle import Turtle, Screen

# turtle object
tmnt = Turtle()
tmnt.shape("turtle")
tmnt.color("turquoise") # change colour

for _ in range(0,4):
    tmnt.forward(200)   # move Turtle 200 paces
    tmnt.right(90)  # turn turtle right 90 degrees

'''Dotted square'''
for _ in range(0, 4):
    tmnt.left(90)
    tmnt.forward(30)
    tmnt.penup()
    tmnt.forward(30)
    tmnt.pendown()
    tmnt.forward(30)




# screen object
screen = Screen()
screen.exitonclick()    # exit when button is clicked