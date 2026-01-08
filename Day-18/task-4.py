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
tim=turtle.Turtle()
tim.pensize(10)
list_of_angles = [45,120,51,60,72,90]
while True:
    tim.color(random.choice(colors))
    tim.fd(100)
    tim.left(random.choice(list_of_angles))