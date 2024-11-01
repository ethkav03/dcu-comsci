class Triathlete(object):
  def __init__(self, name, tid):
    self.name = name
    self.tid = tid
    self.times = {}
    self.race_time = 0

  def add_time(self, sport, time):
    self.times[sport] = time
    self.race_time += time

  def get_time(self, sport):
    return self.times[sport]

  def __str__(self):
    return 'Name: {}\nID: {}\nRace time: {}'.format(self.name, self.tid, self.race_time)
