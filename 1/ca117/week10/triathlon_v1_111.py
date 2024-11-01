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

  def __eq__(self, other):
    return self.race_time == other.race_time

  def __lt__(self, other):
    return self.race_time < other.race_time

  def __gt__(self, other):
    return self.race_time > other.race_time

  def __str__(self):
    return 'Name: {}\nID: {}\nRace time: {}'.format(self.name, self.tid, self.race_time)

class Triathlon(object):
  def __init__(self, athletes=None):
    self.athletes = [] if athletes is None else athletes

  def add(self, athlete):
    if athlete not in self.athletes:
      self.athletes.append(athlete)

  def remove(self, tid):
    for athlete in self.athletes:
      if athlete.tid == tid:
        return self.athletes.remove(athlete)

  def lookup(self, tid):
    for athlete in self.athletes:
      if athlete.tid == tid:
        return athlete
