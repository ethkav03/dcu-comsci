class Score(object):
  def __init__(self, goals=0, points=0):
    self.goals = goals
    self.points = points

  def goals2points(self):
    return (self.goals * 3) + self.points

  def isinstance(self, typeof):
    return type(self) == typeof

  def __eq__(self, other):
    return ((self.goals2points()) == (other.goals2points()))

  def __lt__(self, other):
    return ((self.goals2points()) < (other.goals2points()))

  def __le__(self, other):
    return ((self.goals2points()) <= (other.goals2points()))

  def __add__(self, other):
    goals = self.goals + other.goals
    points = self.points + other.points
    return Score(goals, points)

  def __iadd__(self, other):
    self.goals += other.goals
    self.points += other.points
    return self

  def __str__(self):
    return '{:d} goal(s) and {:d} point(s)'.format(self.goals, self.points)
