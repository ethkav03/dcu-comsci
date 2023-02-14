class MP3Track(object):
  def __init__(self, title, duration):
    self.title = title
    self.duration = duration

  def __str__(self):
    a = []
    a.append('Title: {}'.format(self.title))
    a.append('Duration: {}'.format(self.duration))
    return '\n'.join(a)
