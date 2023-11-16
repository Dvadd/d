from turtle import Turtle

a = Turtle ()
a.color('pink')
a.width (5)

def square():
    a.speed(1)
    a.forward(90)
    a.right(60)
    a.forward(90)
    a.right(60)
    a.forward(90)
    a.right(60)
    a.forward(90)
    a.right(60)
    a.forward(90)
    a.right(60)
    a.forward(90)
    a.right(60)
square()

a.screen.mainloop()