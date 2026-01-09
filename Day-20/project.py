import turtle
game_status= None
screen= turtle.Screen()
screen.setup(width=700,height=700)
screen.bgcolor("black")
screen.title("project-day-20")
score = -3
turtles=[]
for _ in range (3):
    tim =turtle.Turtle()
    tim.color("white")
    tim.penup()
    tim.shape("square")
    turtles.append(tim)
for t in turtles:
    t.goto(score*24,0)
    score +=1

def move_fd():
    while True:
        for i in turtles:
            i.fd(10)
def move_bk():
    while True:
        for i in turtles:
            i.bk(10)
def move_rt():
    for i in turtles:
        i.rt(60)
def move_lt():
    for i in turtles:
        i.lt(60)
screen.listen()
screen.onkey(move_fd,"w")
screen.onkey(move_bk,"s")
screen.onkey(move_lt,"a")
screen.onkey(move_rt,"d")


screen.mainloop()