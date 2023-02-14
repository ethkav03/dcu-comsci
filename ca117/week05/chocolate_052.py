#!usr/bin/env python3

import sys

def count_bars(calories):
   if calories == 0:
      return 0
   elif calories % cals == 0:
      return calories // cals
   else:
      return calories // cals + 1


cals = 400

for line in sys.stdin:
   n = int(line.strip())
   print(count_bars(n))
