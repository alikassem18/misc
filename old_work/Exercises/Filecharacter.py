# Average number of characters per line.

a = open('xo.txt')
b = a.read()
a.close()
c = len(b)
d = b.count('\n')+1
print(c/d)