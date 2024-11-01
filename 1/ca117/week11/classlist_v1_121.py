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
    self.students = [] if students is None else students

  def add(self, student):
    if student not in self.students:
      self.students.append(student)

  def remove(self, cao):
    for student in self.students:
      if student.cao == cao:
        self.students.remove(student)

  def lookup(self, cao):
    for student in self.students:
      if student.cao == cao:
        return student
      return None
