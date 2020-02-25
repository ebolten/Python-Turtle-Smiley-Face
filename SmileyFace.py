import turtle
from turtle import Screen

turtle = turtle.Turtle() # define turtle object
screen = Screen() # define screen
# turtle.speed(0)
screen.setup(480,370)

# head
turtle.penup()
turtle.left(90)
turtle.forward(-60)
turtle.pendown()
turtle.right(90)
turtle.circle(100)

# eyes
turtle.penup()
turtle.goto(55,60)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.goto(-50,60)
turtle.pendown()
turtle.circle(10)

# smile
turtle.penup()
turtle.goto(-60,20)
turtle.right(90)
turtle.pendown()
for i in range(61):
    turtle.forward(3)
    turtle.left(3)

# move cursor away from drawing
turtle.penup()
turtle.goto(-100,-100)
