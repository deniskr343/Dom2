import turtle
def olya(x,y)
    mainTurtle = turtle.Turtle()
    mainTurtle.penup()
    mainTurtle.goto(x,y)
    mainTurtle.pendown()
    mainTurtle.pencolor("yellow")
    mainTurtle.forward(300)
    mainTurtle.left(100)
    mainTurtle.forward(200)
    mainTurtle.left(80)
    mainTurtle.forward(230)
    mainTurtle.left(80)
    mainTurtle.forward(200)
mainTurtle.hideturtle()


turtle.exitonclick()