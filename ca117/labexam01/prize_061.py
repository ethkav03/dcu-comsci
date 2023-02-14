#!/usr/bin/env python3

import sys

def swap(s):
  for swap in swaps:
    tmp = a[d[swap][0]]
    a[d[swap][0]] = a[d[swap][1]]
    a[d[swap][1]] = tmp

  i = 0
  while i < len(a) and a[i] != 'x':
    i += 1
  return i + 1


try:
  pos = int(sys.stdin.readline().strip()) - 1
except ValueError:
  exit()
swaps = sys.stdin.readline().strip()

a = ['A', 'B', 'C']

a[pos] = 'x'

d = {
  'A': (0, 1),
  'B': (1, 2),
  'C': (0, 2),
}

print(swap(swaps))
