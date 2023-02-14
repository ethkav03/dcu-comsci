class Stack(object):
  def __init__(self, a=None):
    self.a = [] if a is None else a

  def push(self, s):
    self.a.append(s)

  def pop(self):
    if len(self.a) > 0:
      return self.a.pop()
    return None

  def top(self):
    return self.a[-1]

  def is_empty(self):
    return len(self.a) == 0

  def __len__(self):
    return len(self.a)

def matcher(line):
  d = {
    ')': '(',
    '}': '{',
    ']': '[',
  }

  s = Stack()

  for c in line:
    if c in d.values():
      s.push(c)
    if c in d.keys():
      if s.pop() != d[c]:
        return False
  return s.is_empty()
