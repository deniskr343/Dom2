import turtle
mainTurtle = turtle.Turtle()
<<<<<<< HEAD
#Синтаксическая ошибка
=======
>>>>>>> 2109c70aa4f636da49ba74f52ff0681f554a44ec
def olya(x,y):
    mainTurtle.penup()
    mainTurtle.goto(x,y)
    mainTurtle.pendown()
    mainTurtle.pencolor("yellow")
    mainTurtle.forward(50)
    mainTurtle.left(100)
    #Движения по 50 или 33
    mainTurtle.forward(33)
    mainTurtle.left(80)
    mainTurtle.forward(50)
    mainTurtle.left(80)
    mainTurtle.forward(33)
#Вызов функции
olya(100,100)

mainTurtle.hideturtle()

turtle.exitonclick()