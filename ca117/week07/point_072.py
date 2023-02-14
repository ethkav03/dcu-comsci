class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, points):
        distance = (((self.x - points.x) * (self.x - points.x)) + ((self.y - points.y) * (self.y - points.y))) ** 0.5
        if distance < 0:
            return distance * -1
        else:
            return distance

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)
