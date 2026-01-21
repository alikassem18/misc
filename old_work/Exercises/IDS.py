# Create a dict from a file.

with open('IDS.txt') as x:
  y = x.read()
z = y.split('\n')
F = {}
a = y.count('\n') + 1
b = a // 6
for c in range(b):
  S = {'First Name': z[1+c*6], 'Last Name': z[2+c*6], 'Age': z[3+c*6], 'Height': z[4+c*6], 'Gender': z[5+c*6]}
  F[z[0+c*6]]= S
from pprint import pprint
pprint(F)
print(F)