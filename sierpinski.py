import turtle
import random
from math import sqrt

def center(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def draw():
    turtle.setworldcoordinates(-0.1, -0.1, 1.1, 1.1)
    turtle.delay(0)
    turtle.hideturtle()

    A = [0, 0]
    B = [1, 0]
    C = [0.5, sqrt(3)/2]
    P0 = [0.1, 0.5]

    turtle.setpos(A)
    turtle.dot(12, "blue")
    turtle.setpos(B)
    turtle.dot(12, "blue")
    turtle.setpos(C)
    turtle.dot(12, "blue")
    turtle.setpos(A)

    turtle.penup()

    turtle.setpos(P0)
    turtle.dot(12, "red")

    ITERATION_COUNT = 7000

    P = P0
    for i in range(ITERATION_COUNT):
        dice = random.randrange(3)
        if dice == 0:
            P = center(P, A)
        elif dice == 1:
            P = center(P, B)
        elif dice == 2:
            P = center(P, C)
        turtle.setpos(P)
        turtle.dot(3)

    turtle.exitonclick()

if __name__ == "__main__":
    draw()
