class MP3Track(object):
  def __init__(self, title, duration, artists=None):
    self.title = title
    self.duration = duration
    self.artists = [] if artists is None else artists

  def __str__(self):
    a = []
    a.append('Title: {}'.format(self.title))
    a.append('By: {}'.format(', '.join(self.artists)))
    a.append('Duration: {}'.format(self.duration))
    return '\n'.join(a)
