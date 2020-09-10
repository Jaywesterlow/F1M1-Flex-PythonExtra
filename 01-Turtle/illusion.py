import turtle

turtle.speed(5)
turtle.bgcolor("black")
turtle.pencolor("white")
turtle.penup()


#setting start pos
turtle.left(135)
turtle.forward(60)
turtle.right(90)

#Start A fill
turtle.pendown()
turtle.forward(60)
turtle.right(45)
turtle.forward(85)
turtle.left(45)
turtle.forward(60)
turtle.left(135)
turtle.forward(170)
turtle.left(45)
turtle.forward(120)
turtle.left(135)
turtle.forward(85)

#Start C fill
turtle.right(90)
turtle.forward(85)
turtle.left(90)
turtle.forward(85)
turtle.right(90)
turtle.forward(85)
turtle.right(90)
turtle.forward(170)
turtle.right(90)
turtle.forward(170)
turtle.penup()

#Next pos
turtle.left(180)
turtle.forward(170)
turtle.left(90)
turtle.forward(170)

#Start C fill
turtle.pendown()
turtle.left(45)
turtle.forward(120)
turtle.left(45)
turtle.forward(170)
turtle.penup()
turtle.left(135)
turtle.forward(60)
turtle.left(45)
turtle.pendown()
turtle.forward(85)
turtle.right(45)
turtle.forward(60)

#Next pos
turtle.penup()
turtle.right(180)
turtle.forward(60)
turtle.left(135)
turtle.pendown()

#1st middle line
turtle.forward(85)
turtle.penup()

#Next pos
turtle.left(45)
turtle.forward(60)
turtle.left(180)
turtle.pendown()

#D, E and F fill
turtle.forward(60)
turtle.left(45)
turtle.forward(85)

turtle.done()