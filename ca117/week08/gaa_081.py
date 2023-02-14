class Score(object):
  def __init__(self, goals=0, points=0):
    self.goals = goals
    self.points = points

  def __str__(self):
    return '{:d} goal(s) and {:d} point(s)'.format(self.goals, self.points)
