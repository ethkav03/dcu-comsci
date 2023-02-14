class Student(object):
  def __init__(self, name, cao):
    self.name = name
    self.cao = cao
    self.grades = {}

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

  def most_popular_subject(self):
    d = {}
    for student in self.students:
      for grade in student.grades:
        if grade in d:
          d[grade] += 1
        else:
          d[grade] = 1
    return sorted(d)[0]

  def __str__(self):
    i = 0
    while i < len(self.students) - 1:
      p = i
      j = i + 1
      while j < len(self.students):
        if self.students[p].cao > self.students[j].cao:
          p = j
        j += 1
      tmp = self.students[i]
      self.students[i] = self.students[p]
      self.students[p] = tmp
      i += 1

    a = []
    for student in self.students:
      a.append('{}'.format(student))
    return '\n'.join(a)
