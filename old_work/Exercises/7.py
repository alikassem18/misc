a = input("Enter any phrase: ")
b = []
c = []
d = ""
for e in a:
  b.append(e)
for f in range(len(a)+1):
  c.append(f)
c.remove(0)
for g in c:
  h = b[-g]
  d = d + h
print(d)