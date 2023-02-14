#!/usr/bin/env python3

import sys

args = sys.argv[1:]

n = int(args[0])

i = 0
while i < n // 2:
   print(" " * (n // 2 - i) + "*" + "**" * i)
   i += 1

i = 0
while i < n // 2 + 1:
   print(" " * i + "*" + "**" * (n // 2 - i))
   i += 1
