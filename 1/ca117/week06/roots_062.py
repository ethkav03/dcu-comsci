#!/usr/bin/env python3

import sys
from math import sqrt

def find_roots(a, b, c):
   try:
      r2 = ((b + sqrt((b * b) - (4 * a * c))) / (2 * a)) * -1
      r1 = ((b - sqrt((b * b) - (4 * a * c))) / (2 * a)) * -1
   except ValueError:
      return None
   return [r1, r2]


for line in sys.stdin:
   nums = line.strip().split()
   abc = []
   for n in nums:
      try:
         abc.append(int(n))
      except ValueError:
         break
   [a, b, c] = abc
   roots = find_roots(a, b, c)
   if find_roots(a, b, c) is not None:
      print(f'r1 = {roots[0]}, r2 = {roots[1]}')
   else:
      print(None)
