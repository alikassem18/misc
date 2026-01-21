# Rock Paper Scissors (partially).

import random

a = ['Rock', 'Paper', 'Scissors']
pc = random.randrange(a)
x = True
while x:
  me = input('rock, paper, scissors: ')
  if me != pc:
    if me == 'Rock' and pc == 'Paper':
      print('me wins!')