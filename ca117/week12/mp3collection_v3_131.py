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

  def get_mp3s_by_artist(self, artist):
    tracks = []
    for track in self.mp3s:
      for s in track.artists:
        if s == artist:
          tracks.append(track)
    return tracks

  def __add__(self, other):
    col = MP3Collection()
    for track in self.mp3s:
      col.mp3s.append(track)
    for track in other.mp3s:
      col.mp3s.append(track)
    return col
