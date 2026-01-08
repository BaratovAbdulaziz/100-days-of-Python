import turtle,random
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

Tim = turtle.Turtle()
screen = turtle.Screen()

def shape1():
    global Tim,colors
    Tim.color(random.choice(colors))
    for _ in range(4):
        Tim.fd(100)
        Tim.left(90)

def shape2():
    for _ in range(5):
        Tim.fd(100)
        Tim.left(72)

def shape3():
    for _ in range(6):
        Tim.fd(100)
        Tim.left(60)

def shape4():
    for _ in range(7):
        Tim.fd(100)
        Tim.left(51)

def shape5():
    for _ in range(3):
        Tim.fd(100)
        Tim.left(120)

def shape6():
    for _ in range(8):
        Tim.fd(100)
        Tim.left(45)
while True:
    random_number=random.randint(1,7)
    if random_number == 1:
        shape1()
    elif random_number == 2:
        shape2()
    elif random_number == 3:
        shape3()
    elif random_number == 4:
        shape4()
    elif random_number == 5:
        shape5()
    elif random_number == 6:
        shape6()
        continue

screen.exitonclick()