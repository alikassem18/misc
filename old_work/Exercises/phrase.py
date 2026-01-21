# Character counter.

a = input('Enter any phrase: ')
b = {}
for c in a:
  if c not in b:
    d = a.count(c)
    b[c] = d
print(b)