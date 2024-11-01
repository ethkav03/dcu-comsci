class Queue(object):
  def __init__(self, q=None):
    self.q = [] if q is None else q

  def enqueue(self, s):
    self.q.append(s)

  def dequeue(self):
    return self.q.pop(0)

  def first(self):
    return self.q[0]

  def is_empty(self):
    return len(self.q) == 0

  def __len__(self):
    return len(self.q)
