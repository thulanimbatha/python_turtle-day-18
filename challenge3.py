from turtle import Turtle, Screen

spider = Turtle()
spider.shape("turtle")
spider.color("green")

'''Move in a Triangle'''
def drawTri():
    spider.pencolor("silver")
    for _ in range(0, 3):
        spider.forward(100)
        spider.left(120)

'''Move in a square'''
def drawSquare():
    spider.pencolor("black")
    for _ in range(0, 4):
        spider.forward(100)
        spider.right(90)

'''Move in a pentagon'''
def drawPent():
    spider.pencolor("purple")
    for _ in range(0, 5):
        spider.forward(100)
        spider.left(72)

'''Move in a Hexagon'''
def drawHex():
    spider.pencolor("blue")
    for _ in range(0, 6):
        spider.forward(100)
        spider.right(60)

'''Move in a Heptagon'''
def drawHept():
    spider.pencolor("green")
    for _ in range(0, 7):
        spider.forward(100)
        spider.left(51.43)

'''Move in a Octagon'''
def drawOct():
    spider.pencolor("yellow")
    for _ in range(0, 8):
        spider.forward(100)
        spider.right(45)

'''Move in a Nonagon'''
def drawNon():
    spider.pencolor("orange")
    for _ in range(0, 9):
        spider.forward(100)
        spider.left(40)

'''Move in a Decagon'''
def drawDec():
    spider.pencolor("red")
    for _ in range(0, 10):
        spider.forward(100)
        spider.right(36)

drawTri()
drawSquare()
drawPent()
drawHex()
drawHept()
drawOct()
drawNon()
drawDec()


screen = Screen()
screen.exitonclick()