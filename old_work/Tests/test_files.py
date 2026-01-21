with open('ali.txt','w') as x:
  x.write("hi")

with open('ali.txt','a') as x:
  x.write("hello")


with open('ali.txt') as x:
  y = x.read()
print(y)
print(help(open))