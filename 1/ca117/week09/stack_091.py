class Stack(object):
  def __init__(self, a=None):
    self.a = [] if a is None else a

  def push(self, s):
    self.a.append(s)

  def pop(self):
    return self.a.pop()

  def top(self):
    return self.a[-1]

  def is_empty(self):
    return len(self.a) == 0

  def __len__(self):
    return len(self.a)
