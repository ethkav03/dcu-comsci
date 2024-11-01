#!/usr/bin/env python3

import sys

a = []
for line in sys.stdin:
  a.append(line.strip())

b = []
c = []

i = 0
while i < len(a):
  b.append(a[i])
  try:
    c.append(a[i + 1])
  except IndexError:
    break
  i += 2

for s in b:
  print(s)

for s in c[::-1]:
  print(s)
