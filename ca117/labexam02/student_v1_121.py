class Student(object):
  def __init__(self, name, cao):
    self.name = name
    self.cao = cao

  def __str__(self):
    a = []
    a.append('Name: {}'.format(self.name))
    a.append('CAO: {}'.format(self.cao))
    return '\n'.join(a)
