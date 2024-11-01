#!/usr/bin/env python3

import sys

for line in sys.stdin:
   d = {}
   a = line.strip().split()
   for num in a:
      if num not in d:
         d[num] = 1
      else:
         d[num] += 1

   e = []
   for k, v in d.items():
      if v == 1:
         e.append(k)

   low = sorted(e)

   if len(e) > 0:
      print(low[-1])
   else:
      print('none')
