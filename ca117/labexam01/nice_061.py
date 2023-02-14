#!/usr/bin/env python3

import sys

for line in sys.stdin:

   d = {
      'n': 0,
      'i': 0,
      'c': 0,
      'e': 0,
   }

   s = line.strip()
   for c in s:
      if c in d:
         d[c] += 1
   i = 0
   for c in d:
      if d[c] != 1:
         break
      else:
         i += 1

   if i == 4:
      print(s)
