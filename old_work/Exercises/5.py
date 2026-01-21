a = input("Enter a natural number: ")
b = int(a)
if b < 0:
  print("rejected")
for c in range(1, b + 1):
  d = " " * (b - c)
  e = "*" * c
  print(d + e)
