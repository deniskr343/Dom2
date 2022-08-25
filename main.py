import turtle

mainTurtle = turtle.Turtle()

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