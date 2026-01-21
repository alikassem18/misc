a = input('Enter any number: ')
b = int(a)
c = input('ones,tens,etc...: ')
d = int(c)
e = b % (d*10)
f = e // d
print(f)