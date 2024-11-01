#!/usr/bin/env python3

import sys

nums = sys.stdin.readline().strip().split()

try:
  a = []
  for n in nums:
    a.append(int(n))
except ValueError:
  exit()

[X, Y, N] = a

for i in range(1, N + 1):
  if i % X == 0 and i % Y == 0:
    print('fizzbuzz')
  elif i % X == 0:
    print('fizz')
  elif i % Y == 0:
    print('buzz')
  else:
    print(i)
