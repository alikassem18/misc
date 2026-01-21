#given an integer, print every integer less than it, that has the property that it is equal to its sum of divisors.

a = input()
if a == '0' or a == '1':
  exit()
b = int(a)
c = []
for d in range(2,b+1):
  e = 0
  for f in range(1,d):
    if d%f == 0:
      e = e + f
  if e == d:
    c.append(e)
print(c)