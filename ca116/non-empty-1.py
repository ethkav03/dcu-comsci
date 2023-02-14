#!/usr/bin/env python3

import sys

a = sys.argv[1:]
total = 0

i = 0
while i < len(a):
   if a[i] != "":
      total += 1
   i += 1

print(total)
