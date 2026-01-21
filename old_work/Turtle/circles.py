# Drawing circles using turtle.

import turtle

x = input('')

turtle.speed(0)
turtle.ht()
turtle.width(5)
turtle.setpos(0,-380)
for y in range(1,int(x)):
    turtle.circle(10*y,360)

turtle.exitonclick()