class Student(object):
  def __init__(self, name, cao):
    self.name = name
    self.cao = cao

  def __str__(self):
    a = []
    a.append('Name: {}'.format(self.name))
    a.append('CAO: {}'.format(self.cao))
    return '\n'.join(a)

class Classlist(object):
  def __init__(self, students=None):
    self.students = {} if students is None else students

  def add(self, student):
    if student not in self.students:
      self.students[student.cao] = student

  def remove(self, cao):
    if cao in self.students:
      del self.students[cao]

  def lookup(self, cao):
    if cao in self.students:
      return self.students[cao]
    return None
