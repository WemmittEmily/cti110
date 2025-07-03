#Emily Wemmitt
#7/3/25
#P4LAB1
#Make a sqaure and a triangle using turtle

import turtle
win = turtle.Screen()
t = turtle.Turtle()
number_of_sides_drawn = 0

t.pensize(3)
t.pencolor("green")
t.shape("turtle")

while number_of_sides_drawn < 3:
    t.forward(200)
    t.left(120)
    number_of_sides_drawn += 1

win.mainloop()
