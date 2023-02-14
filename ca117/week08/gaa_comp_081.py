class Score(object):
  def __init__(self, goals=0, points=0):
    self.goals = goals
    self.points = points

  def goals2points(self):
    return (self.goals * 3) + self.points

  def __eq__(self, other):
    return ((self.goals2points()) == (other.goals2points()))

  def __lt__(self, other):
    return ((self.goals2points()) < (other.goals2points()))

  def __le__(self, other):
    return ((self.goals2points()) <= (other.goals2points()))

  def __str__(self):
    return '{:d} goal(s) and {:d} points'.format(self.goals, self.points)
