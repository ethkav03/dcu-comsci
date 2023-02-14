#!/usr/bin/env python3

import sys

args = sys.argv[1:]

sum = 0

i = 0
while i < len(args):
   sum += int(args[i])
   i += 1

print(sum)
