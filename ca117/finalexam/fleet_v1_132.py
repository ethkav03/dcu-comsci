class Vehicle(object):
  def __init__(self, vin, cat, mileage, drivers=None):
    self.vin = vin
    self.cat = cat
    self.mileage = mileage
    self.drivers = [] if drivers is None else drivers

  def __str__(self):
    a = []
    a.append('ID: {}'.format(self.vin))
    a.append('Category: {}'.format(self.cat))
    a.append('Mileage: {}'.format(self.mileage))
    a.append('Drivers: {}'.format(', '.join(self.drivers)))
    return '\n'.join(a)

class Fleet(object):
  def __init__(self, fleet=None):
    self.fleet = {} if fleet is None else fleet

  def add(self, vehicle):
    if vehicle.vin not in self.fleet:
      self.fleet[vehicle.vin] = vehicle

  def remove(self, vehicle):
    if vehicle in self.fleet:
      del self.fleet[vehicle]

  def lookup(self, vehicle):
    if vehicle in self.fleet:
      return self.fleet[vehicle]
