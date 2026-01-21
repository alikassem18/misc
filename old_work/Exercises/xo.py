# XO board checker.

with open('c:/Users/Ali/Desktop/PYTHON/replit/randoms/xo.txt') as a:
  b = a.read()
d = []
for c in b:
  if c == 'x' or c == 'o':
    d.append(c)

if d[0] == d[1] == d[2]:
  print(d[0],'Wins')
elif d[3] == d[4] == d[5]:
  print(d[3],'Wins')
elif d[6] == d[7] == d[8]:
  print(d[6],'Wins')
elif d[0] == d[3] == d[6]:
  print(d[0],'Wins')
elif d[1] == d[4] == d[7]:
  print(d[1],'Wins')
elif d[2] == d[5] == d[8]:
  print(d[2],'Wins')
elif d[0] == d[4] == d[8]:
  print(d[0],'Wins')
elif d[2] == d[4] == d[6]:
  print(d[2],'Wins')
else:
  print('Draw')