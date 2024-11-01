from math import sqrt

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


binops = {'+': float.__add__,
          '-': float.__sub__,
          '*': float.__mul__,
          '/': float.__truediv__}

uniops = {'n': float.__neg__,
          'r': sqrt}

def calculator(line):
  a = line.split()
  nums = Stack()
  for s in a:
    if s in binops:
      y = nums.pop()
      x = nums.pop()
      nums.push(binops[s](x, y))
    elif s in uniops:
      nums.push(uniops[s](nums.pop()))
    else:
      nums.push(float(s))
  return nums.top()
