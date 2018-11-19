import turtle
from random import randint
u = 0
turtle.speed(1000000000)
turtle.delay(0)
#turtle.tracer(0, 0)

def koch(x, m):  
    if x < m:
        turtle.forward(x)
    else:
         koch(x / 3, m)
         turtle.left(60)
         koch(x / 3, m)
         turtle.right(120)
         koch(x / 3, m)
         turtle.left(60)
         koch(x / 3, m)

def repeat():
    u = 0
    for x in range(1):
        koch(500, 5)
        turtle.right(120)
        u += 1
    turtle.right(10)
    if u < 1000000:
        repeat()

repeat()