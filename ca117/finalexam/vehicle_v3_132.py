class Vehicle(object):
  def __init__(self, vin, cat, mileage, drivers=None):
    self.vin = vin
    self.cat = cat
    self.mileage = mileage
    self.drivers = [] if drivers is None else drivers

  def add_driver(self, driver):
    if driver not in self.drivers:
      self.drivers.append(driver)

  def __str__(self):
    a = []
    a.append('ID: {}'.format(self.vin))
    a.append('Category: {}'.format(self.cat))
    a.append('Mileage: {}'.format(self.mileage))
    a.append('Drivers: {}'.format(', '.join(self.drivers)))
    a.append('Service due in {} miles'.format(10000 - int(self.mileage)))
    return '\n'.join(a)
