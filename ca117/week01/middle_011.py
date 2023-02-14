#!/usr/bin/env python3

import sys

for line in sys.stdin:
   s = line.strip()
   if len(s) % 2 == 0:
      print("No middle character!")
   else:
      print(s[len(s) // 2])
