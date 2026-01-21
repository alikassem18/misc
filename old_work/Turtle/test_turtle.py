from turtle import *
s = 75
n = input('')
n = int(n)
a = 180*(n-2)
t = Turtle()
for x in range(n):
    t.fd(s)
    t.lt(180-a/n)
mainloop()