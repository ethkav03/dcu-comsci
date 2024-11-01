#!/usr/bin/env python3

import sys

def doubles(s):
  total = 0
  i = 0
  while i < len(s) - 1:
    if s[i] == s[i + 1]:
      total += 1
      i += 1
    i += 1
  return total


d = {}

for line in sys.stdin:
  s = line.strip()
  d[doubles(s)] = s

a = []
for k, v in sorted(d.items()):
  a.append(v)

print(a[-1])
