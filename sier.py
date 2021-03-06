import turtle
import random

win = turtle.Screen()
t = turtle.Turtle()
win.bgcolor("white")
win.setworldcoordinates(0, 1300, 1300, 0)
t.speed(10)
t.shape("turtle")
color = ['red', 'yellow', 'orange', 'green', 'blue', 'skyblue', 'purple', 'pink', 'cyan', 'magenta']

def drawTriangle(x, y, length, turtle):
    turtle.color(random.choice(color))
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.goto(x+length, y)
    turtle.goto(x+length/2, y-length)
    turtle.goto(x, y)

def drawSier(x, y, length, turtle, depth):
    if depth > 0:
        drawSier(x+length/2, y, length/2, turtle, depth-1)
        drawSier(x+length/4, y-length/2, length/2, turtle, depth-1)
        drawSier(x, y, length/2, turtle, depth-1)
    if depth == 0:
        drawTriangle(x, y, length, turtle)
d = int(input("반복할 횟수 :"))
drawSier(200, 800, 600, t, d)
