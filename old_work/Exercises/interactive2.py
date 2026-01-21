# Guessing numbers game.

from random import randint

while True:
  a = randint(2,17)
  b = input('Guess the number: ')
  if b == 'Q':
    break
  while True:
    if int(b) < a:
      print('Try larger: ')
    elif int(b) > a:
      print('Try smaller: ')
    else:
      break
    b = input('')
  print('Cool!')