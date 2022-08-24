import turtle

mainTurtle = turtle.Turtle()

def danik(x,y):
    mainTurtle.penup()
    mainTurtle.goto(x,y)
    mainTurtle.pendown()
    mainTurtle.fillcolor('yellow')
    mainTurtle.begin_fill()
    #Тут можно оптимизировать циклом for
    mainTurtle.forward(90)
    mainTurtle.right(90)
    mainTurtle.forward(90)
    mainTurtle.right(90)
    mainTurtle.forward(90)
    mainTurtle.right(90)
    mainTurtle.forward(90)
    mainTurtle.end_fill()
danik(100,100)


mainTurtle.hideturtle()
turtle.exitonclick()