from turtle import Turtle, Screen

# turtle object
tmnt = Turtle()
tmnt.shape("turtle")
tmnt.color("turquoise") # change colour

for _ in range(0,4):
    tmnt.forward(200)   # move Turtle 200 paces
    tmnt.right(90)  # turn turtle right 90 degrees






# screen object
screen = Screen()
screen.exitonclick()    # exit when button is clicked