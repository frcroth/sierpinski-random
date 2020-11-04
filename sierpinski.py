import turtle
import random
from math import *

turtle.setworldcoordinates(-0.1,-0.1,1.1,1.1)
turtle.delay(0)
turtle.hideturtle()

A=[0,0]
B=[1,0]
C=[0.5,sqrt(3)/2]
P0=[0.1,0.5]

turtle.setpos(A)
turtle.dot(12,"blue")
turtle.setpos(B)
turtle.dot(12,"blue")
turtle.setpos(C)
turtle.dot(12,"blue")
turtle.setpos(A)

turtle.penup()

turtle.setpos(P0)
turtle.dot(12,"red")

def center(p1,p2):
    return ( (p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

i=1
P=P0
while i <= 7000:
    wuerfel = random.randrange(3)
    if wuerfel ==0:
        P = center(P,A)
    if wuerfel ==1:
        P = center(P,B)
    if wuerfel ==2:
        P = center(P,C)
    turtle.setpos(P)
    turtle.dot(3)
    i = i + 1

turtle.exitonclick()























