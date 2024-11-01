#!/usr/bin/env python3

import sys

pos = sys.stdin.readline().strip()
swaps = sys.stdin.readline().strip()

cups = [1, 2, 3]

cups[int(pos) - 1] = 'x'

for c in swaps:
   if c == 'A':
      tmp = cups[0]
      cups[0] = cups[1]
      cups[1] = tmp
   elif c == 'B':
      tmp = cups[1]
      cups[1] = cups[2]
      cups[2] = tmp
   else:
      tmp = cups[0]
      cups[0] = cups[2]
      cups[2] = tmp

i = 0
while i < len(cups) and cups[i] != 'x':
   i += 1

print(i + 1)
