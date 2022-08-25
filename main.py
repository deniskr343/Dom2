import turtle

mainTurtle = turtle.Turtle()
#Функция в которой создается квадрат. Все что ниже должно быть в функции
#Функция должна также перемещать в координты х и у, которые передаются в неё. penup() потом goto(x,y) и pendown()
mainTurtle.pensize(6)
#квадрат
mainTurtle.color("green")
mainTurtle.pendown()
mainTurtle.right(45)
mainTurtle.forward(150)
mainTurtle.left(90)
mainTurtle.forward(150)
mainTurtle.left(90)
mainTurtle.forward(150)
mainTurtle.left(90)
mainTurtle.forward(150)
mainTurtle.penup()

mainTurtle.hideturtle()
turtle.exitonclick()
