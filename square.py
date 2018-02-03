
import turtle
me=turtle.Turtle()
me.filling()
n=int(input('enter the side of the square :'))
m=int(input('enter the distance between the squares :'))
def square(n):
    for i in range (4):
        me.pensize(2)
        me.color('blue')
        me.lt(90)
        me.fd(n)
def turn():
    me.color('white')
    me.fd(m/2)
    me.rt(90)
    me.fd(m/2)
    me.lt(90)
for i in range (10):
    square(n)
    turn()
    n += m

