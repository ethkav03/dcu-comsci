#!/usr/bin/env python3

import sys

for line in sys.stdin:
   s = line[1:-2].strip()
   if len(s) > 0:
      print(s)
