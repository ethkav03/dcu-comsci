def maximum(a):
  if len(a) == 1:
    return a[0]
  return a[0] if a[0] > maximum(a[1:]) else maximum(a[1:])
