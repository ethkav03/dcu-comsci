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

  def most_popular_subject(self):
    d = {}
    for student in self.students.values():
      for subject in student.grades:
        if subject in d:
          d[subject] += 1
        else:
          d[subject] = 1
    a = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return a[0][0]

  def __str__(self):
    self.students = sorted(self.students.values(), key=lambda x: x.cao)

    a = []
    for student in self.students:
      a.append('{}'.format(student))
    print('{}'.format(a))
