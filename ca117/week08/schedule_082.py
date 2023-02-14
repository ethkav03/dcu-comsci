class Meeting(object):
  def __init__(self, hour, minute, duration):
    self.hour = hour
    self.minute = minute
    self.duration = duration

  def __str__(self):
    return '{:0>2}:{:0>2} ({} minutes)'.format(self.hour, self.minute, self.duration)

class Schedule(object):
  def __init__(self, a=None):
    self.a = [] if a is None else []

  def add(self, meeting):
    self.a.append(meeting)

  def __str__(self):
    meetings = []
    for meeting in self.a:
      meetings.append('{}'.format(meeting))
    return 'Schedule\n--------\n{}\nMeetings today: {}'.format(
      '\n'.join(sorted(meetings)), len(meetings))
