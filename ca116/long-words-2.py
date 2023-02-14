#!/usr/bin/env python3

import sys

a = sys.argv[1:]

i = 0
while i < len(a) and len(a[i]) < 6:
   i += 1

if i < len(a):
   print(a[i])
