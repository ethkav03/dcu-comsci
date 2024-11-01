class MP3Track(object):
  def __init__(self, title, duration):
    self.title = title
    self.duration = duration

  def __str__(self):
    a = []
    a.append('Title: {}'.format(self.title))
    a.append('Duration: {}'.format(self.duration))
    return '\n'.join(a)

class MP3Collection(object):
  def __init__(self, mp3s=None):
    self.mp3s = [] if mp3s is None else mp3s

  def add(self, mp3):
    self.mp3s.append(mp3)

  def remove(self, track):
    for mp3 in self.mp3s:
      if mp3.title == track:
        self.mp3s.remove(mp3)
        break

  def lookup(self, track):
    for mp3 in self.mp3s:
      if mp3.title == track:
        return mp3
