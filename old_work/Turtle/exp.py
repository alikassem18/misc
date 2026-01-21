# Drawing with turtle.
import turtle

xa = input('')
xb = input('')

ta = turtle.Turtle()
na = 20
ta.width(2)
ta.speed(0)
ta.pencolor('red')
ta.ht()
ta.lt(90)
for ya in range(1,int(xa)):
    ta.fd(na*ya)
    ta.rt(90)
    ta.fd(na*ya)
    ta.rt(90)

tb = turtle.Turtle()
tb.speed(0)
tb.ht()
tb.width(2)
for z in range(8):
    for yb in range(1,int(xb)):
        tb.circle(10*yb,360)
    tb.up()
    tb.setpos(0,0)
    tb.down()
    tb.lt(45)

turtle.exitonclick()