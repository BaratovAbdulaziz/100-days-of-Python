import turtle
def cube():
    Abdulaziz = turtle.Turtle()
    Abdulaziz.color("red")
    Abdulaziz.forward(100)
    Abdulaziz.left(90)
    Abdulaziz.forward(100)
    Abdulaziz.left(90)
    Abdulaziz.forward(100)
    Abdulaziz.left(90)
    Abdulaziz.forward(100)


def flouwer():
    a=0
    global gamer
    gamer = turtle.Turtle()
    for x in range(1,15):
        gamer.left(90)
        gamer.forward(15)
        gamer.right(10)
        gamer.forward(20)
        gamer.left(50)
        gamer.right(10)
        gamer.forward(30)
        gamer.left(100)
cube()
flouwer()
flouwer()
gamer.penup
gamer.left(180)
gamer.forward(50)
flouwer()