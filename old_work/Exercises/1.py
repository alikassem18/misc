a = input("Enter any phrase:")
b = "0123456789"
c = []
for d in a:
  if d in b:
    e = int(d)
    if e%2 == 0:
      c.append(e)
print("This phrase contains",len(c),"even digits")