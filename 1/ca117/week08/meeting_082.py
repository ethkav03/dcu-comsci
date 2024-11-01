class Meeting(object):
  def __init__(self, hour, minute, duration):
    self.hour = hour
    self.minute = minute
    self.duration = duration

  def __str__(self):
    return '{:0>2}:{:0>2} ({} minutes)'.format(self.hour, self.minute, self.duration)
