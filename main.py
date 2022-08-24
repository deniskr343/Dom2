import turtle

mainTurtle = turtle.Turtle()
def danik(20,20):
    mainTurtle.penup()
    mainTurtle.goto(20,20)
    mainTurtle.pendown()
    mainTurtle.fillcolor('yellow')
    mainTurtle.begin_fill()
    mainTurtle.forward(90)
    mainTurtle.right(90)
    mainTurtle.forward(90)
    mainTurtle.right(90)
    mainTurtle.forward(90)
    mainTurtle.right(90)
    mainTurtle.forward(90)
    mainTurtle.end_fill()



mainTurtle.hideturtle()
turtle.exitonclick()