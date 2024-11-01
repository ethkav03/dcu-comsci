def minimum(a):
  if len(a) == 1:
    return a[0]
  return a[0] if a[0] < minimum(a[1:]) else minimum(a[1:])
