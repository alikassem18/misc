a = open("Adding.txt","r")
b = a.read()
a.close()
c = b.split("\n")
d = 0
for e in c:
  d = d+int(e)
print(d)