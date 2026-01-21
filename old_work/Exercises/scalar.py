# Dot product of vevtors.

A = input('')
B = input('')
C = input('')
D = input('')
a = A.split(' ')
b = B.split(' ')
c = C.split(' ')
d = D.split(' ')
AB = {'X': int(b[0])-int(a[0]), 'Y': int(b[1])-int(a[1])}
CD = {'X': int(d[0])-int(c[0]), 'Y': int(d[1])-int(c[1])}
dot_product = AB['X']*CD['X'] + AB['Y']*CD['Y']
print(dot_product)