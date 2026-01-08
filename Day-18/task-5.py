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
tim = turtle.Turtle()
tim.speed(100)
screen = turtle.Screen()
for _ in range(200):
    tim.color(random.choice(colors))
    tim.circle(100)
    tim.left(50)
screen.exitonclick()