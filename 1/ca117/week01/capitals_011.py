#!/usr/bin/env python3

import sys

for line in sys.stdin:
   s = line.strip()
   if len(s) > 1:
      print(s[0].upper() + s[1:-1] + s[-1].upper())
