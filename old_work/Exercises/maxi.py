# Find max.

a = input('')
b = a.split(' ')
while len(b) > 1:
  if int(b[0]) <= int(b[1]):
    b.remove(b[0])
  else:
    b.remove(b[1])
print(b)