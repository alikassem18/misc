x = input('')
y = x.split(" ")
b = 'a'
c = 0
for d in y:
  if d.isalpha():
    b = d
  else:
    if b == 's':
      c = c - int(d)
    if b == 'a':
      c = c + int(d)
print(c)