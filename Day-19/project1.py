import turtle
tim = turtle.Turtle()
screen = turtle.Screen()

def fw():
    tim.fd(3)

def bw():
    tim.bk(3)
def lt():
    tim.left(3)
def rt():
    tim.right(3)
def su():
    tim.speed(1)
def nc():
    tim.speed(3)
screen.listen()

screen.onkeypress(fw,"w")
screen.onkeypress(bw,"s")
screen.onkeypress(su,"Up")
screen.onkeypress(rt,"d")
screen.onkeypress(lt,"a")
screen.onkeyrelease(nc,"Up")
screen.onkey(tim.reset,"c")
screen.mainloop()