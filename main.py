import turtle

mainTurtle = turtle.Turtle()
def circlePasha(x,y):
    mainTurtle.penup()
    mainTurtle.goto(x,y)
    mainTurtle.pendown()
    mainTurtle.begin_fill()
    mainTurtle.circle(50)
    mainTurtle.fillcolor('red')
    mainTurtle.end_fill()
circlePasha(100,100)

mainTurtle.hideturtle()
turtle.exitonclick()