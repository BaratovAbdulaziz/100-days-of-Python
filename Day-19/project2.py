import turtle, random

colors = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine",
    "azure", "beige", "bisque", "black", "blanchedalmond",
    "blue", "blueviolet", "brown", "burlywood",
    "cadetblue", "chartreuse", "chocolate", "coral",
    "cornflowerblue", "crimson", "cyan", "darkblue",
    "darkcyan", "darkgoldenrod", "darkgreen", "darkmagenta",
    "darkorange", "darkred", "deeppink", "deepskyblue",
    "gold", "goldenrod", "gray", "green", "hotpink",
    "indianred", "indigo", "khaki", "lavender",
    "lightblue", "lightgreen", "lime", "magenta",
    "maroon", "navy", "olive", "orange", "orchid",
    "pink", "plum", "purple", "red", "salmon",
    "silver", "skyblue", "springgreen", "tan",
    "teal", "tomato", "turquoise", "violet",
    "white", "yellow"
]

turtles = []
screen = turtle.Screen()
screen.setup(width=500, height=200)

def make_move():
    for t in turtles:
        t.fd(random.randint(1, 10))

def make_Turtle():
    start_x = -200
    start_y = -60

    for i in range(1, 8):
        tim = turtle.Turtle(shape="turtle")
        tim.color(random.choice(colors))
        tim.speed(0)
        tim.penup()
        tim.goto(start_x, start_y + i * 20)
        tim.number = i
        turtles.append(tim)

make_Turtle()

bet = screen.numinput("Bet", "1-7", minval=1, maxval=7)

finish_x = screen.window_width() / 2 - 20
winner = None

while winner is None:
    make_move()
    for t in turtles:
        if t.xcor() >= finish_x:
            winner = t.number
            break

print("Winner:", winner)

screen.exitonclick()
