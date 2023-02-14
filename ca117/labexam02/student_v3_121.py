class Student(object):
  def __init__(self, name, cao):
    self.grades = {}
    self.name = name
    self.cao = cao

  def tagger(item):
   return item[1]

  def add_grade(self, subject, grade):
    if subject not in self.grades:
      self.grades[subject] = grade

  def get_grade(self, subject):
    if subject in self.grades:
      return self.grades[subject]
    return 'N/A'

  def calc_points(self):
    d = {
      'H1': 100,
      'H2': 88,
      'H3': 77,
      'H4': 66,
      'H5': 56,
      'H6': 46,
      'H7': 37,
      'H8': 0,
      'O1': 56,
      'O2': 46,
      'O3': 37,
      'O4': 28,
      'O5': 20,
      'O6': 12,
      'O7': 0,
      'O8': 0,
    }
    b = []
    for s in self.grades.values():
      b.append(d[s])
    b = sorted(b, reverse=True)
    #print(b)
    total = 0
    if len(b) < 3:
      i = 0
      while i < len(b):
        total += b[i]
        i += 1
    else:
      i = 0
      while i < 3:
        total += b[i]
        i += 1
    return total

  def __str__(self):
    a = []
    a.append('Name: {}'.format(self.name))
    a.append('CAO: {}'.format(self.cao))
    a.append('Points: {}'.format(self.calc_points()))
    return '\n'.join(a)
