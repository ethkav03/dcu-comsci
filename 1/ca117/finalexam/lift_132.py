#!/usr/bin/env python3

import sys

def count_press(i):
  count = 0
  if s < g:
    while i != g:
      if i < g:
        i += u
        if u == 0:
          return 'Sorry Sheila!'
      else:
        i -= d
        if u == d or d == 0:
          return 'Sorry Sheila!'
      count += 1
  elif s > g:
    while i != g:
      if i < g:
        i += u
        if u == d or u == 0:
          return 'Sorry Sheila!'
      else:
        i -= d
        if d == 0:
          return 'Sorry Sheila!'
      count += 1
  return count


a = sys.stdin.readline().strip().split()
nums = []
for n in a:
  nums.append(int(n))
[f, s, g, u, d] = nums

i = s
if s == g:
  print('0')
else:
  print(count_press(i))
