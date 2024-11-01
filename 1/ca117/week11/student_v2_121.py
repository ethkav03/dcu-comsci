class Student(object):
  def __init__(self, name, cao, grades=None):
    self.grades = {} if grades is None else grades
    self.name = name
    self.cao = cao

  def add_grade(self, subject, grade):
    if subject not in self.grades:
      self.grades[subject] = grade

  def get_grade(self, subject):
    if subject in self.grades:
      return self.grades[subject]
    return 'N/A'

  def __str__(self):
    a = []
    a.append('Name: {}'.format(self.name))
    a.append('CAO: {}'.format(self.cao))
    return '\n'.join(a)
