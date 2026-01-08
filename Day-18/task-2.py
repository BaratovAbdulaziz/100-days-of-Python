import turtle
Tim_the_turtle = turtle.Turtle()
for _ in range(10):

    Tim_the_turtle.fd(10)
    Tim_the_turtle.penup()
    Tim_the_turtle.fd(10)
    Tim_the_turtle.pendown()

screen = turtle.Screen()
screen.exitonclick()