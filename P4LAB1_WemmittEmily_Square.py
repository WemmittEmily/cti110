#Emily Wemmitt
#7/3/25
#P4LAB1
#Make a sqaure and a triangle using turtle

import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(3)
t.pencolor("pink")
t.shape("turtle")

number_of_sides_drawn = 0

while number_of_sides_drawn < 4:
    t.forward(200)

    t.right(90)

    number_of_sides_drawn += 1

win.mainloop()

