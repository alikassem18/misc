class House:
  def __init__(self, area, location, cost, sold = False):
    self.area = area
    self.location = location
    self.cost = cost
    self.sold = sold
  def buy(self, money):
    if self.sold:
      print('Sold')
    else:
      if self.cost <= money:
        print('Congrats!')
      else:
        print('Insufficient funds')
H1 = House(1.4, 'hi', 1000)
H1.buy(500)