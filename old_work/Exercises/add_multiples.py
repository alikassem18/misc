a = 1000
b = range(1,a)
c = 0
for d in b:
  if d%3 == 0:
    c = c+d
  if d%5 == 0:
    c = c+d
print(c)