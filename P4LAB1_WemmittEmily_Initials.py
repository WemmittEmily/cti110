#Emily Wemmitt
#7/3/25
#P4LAB1
#Initials using turtle

import turtle
win = turtle.Screen()
t = turtle.Turtle()

#E

t.pensize(3)
t.pencolor("purple")
t.shape("turtle")

t.left(90)
t.forward(100)

t.right(90)
t.forward(50)

t.backward(50)
t.right(90)
t.forward(50)

t.left(90)
t.forward(40)

t.backward(40)
t.right(90)
t.forward(50)

t.left(90)
t.forward(50)

#W
t.penup()
t.backward(50)
t.forward(20)
t.right(90)
t.forward(100)
t.left(90)
t.forward(20)
t.pendown()

t.right(75)
t.forward(100)
t.left(150)
t.forward(100)
t.right(150)
t.forward(100)
t.left(150)
t.forward(100)

win.mainloop()
