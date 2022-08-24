import turtle

mainTurtle = turtle.Turtle()
def circlePasha(x,y,circle,color):
    mainTurtle.penup()
    mainTurtle.goto(x,y)
    mainTurtle.pendown()
    mainTurtle.begin_fill()
    mainTurtle.circle(circle)
    mainTurtle.fillcolor(color)
    mainTurtle.end_fill()


mainTurtle.hideturtle()
turtle.exitonclick()