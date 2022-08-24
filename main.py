import turtle

mainTurtle = turtle.Turtle()
def Artem(x,y):
    mainTurtle.penup()
    mainTurtle.pencolor('green')
    mainTurtle.goto(x,y)
    mainTurtle.pendown()
    mainTurtle.forward(100)
    mainTurtle.left(120)
    mainTurtle.forward(100)
    mainTurtle.left(120)
    mainTurtle.forward(100)
Artem(x=-50, y=-0)
mainTurtle.hideturtle()
turtle.exitonclick()