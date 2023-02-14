def reverse_list(a):
  if a == []:
    return []
  return [a[-1]] + reverse_list(a[:-1])
