#!/usr/bin/env python3

import sys

def calc_minutes(h, m, z):
  total = 0
  if h == '12' and z == 'a.m.':
    return int(m)
  elif z == 'a.m.':
    return int(h) * 60 + int(m)
  else:
    return int(h) * 60 + int(m) + (12 * 60)


d = {}

for line in sys.stdin:
  time = line.strip()
  [HM, Z] = time.split()
  [H, M] = HM.split(':')

  minutes = calc_minutes(H, M, Z)
  d[minutes] = time

for time in sorted(d.items()):
  print(time[1])
