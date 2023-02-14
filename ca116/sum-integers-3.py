#!/usr/bin/env python3

import sys

args = sys.argv[1:]

total = 0

i = 0
while i < len(args):
   with open(args[i]) as f:
      a = f.readlines()
      j = 0
      while j < len(a):
         total += int(a[j])
         j += 1
   i += 1

print(total)
