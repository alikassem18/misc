from datetime import date

x = date.today()
a = input("Enter a dash-sepersted 'YMD' date: ")
b = x.strftime('%Y-%m-%d')
c = a.split('-')
d = b.split('-')
e = ['Years, ', 'Months, ', 'Days']
f = ''
for g in range(len(c)):
  h = int(d[g]) - int(c[g])
  f = f + str(h) + ' ' + e[g]
print(f)