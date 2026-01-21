# Word counter.

a = input('')
b = a.split(' ')
c = []
x = {}
for d in b:
  if d not in c:
    c.append(d)
for e in c:
  f = a.count(e)
  x[e] = f
print(x)