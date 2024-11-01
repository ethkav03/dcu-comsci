class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def midpoint(self, other):
    x = (self.x + other.x) / 2
    y = (self.y + other.y) / 2
    return Point(x, y)

  def __str__(self):
    return '({:.1f}, {:.1f})'.format(self.x, self.y)
