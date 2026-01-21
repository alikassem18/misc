import random

cards = []
co = 'RBYG'
ch = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 'D2', 'R', 'D4', 'W']

for x in co:
  for y in ch[:-2]:
    z = x+y
    cards.append(z)
cards = cards + cards
for x in co:
  cards.append(x+'0')
  cards = cards + ch[-2:]

random.shuffle(cards)

print(cards)