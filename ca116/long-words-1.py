#!/usr/bin/env python3

import sys

a = sys.argv[1:]

i = 0
while i < len(a):
   if len(a[i]) >= 6:
      print(a[i])
   i += 1
