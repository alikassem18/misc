# Drawing with turtles.

import turtle

x = input('')
n = 20
turtle.width(2)
turtle.speed(10)
turtle.lt(90)
for y in range(1,int(x)):
    turtle.fd(n*y)
    turtle.rt(90)
    turtle.fd(n*y)
    turtle.rt(90)

turtle.exitonclick()