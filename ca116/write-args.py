#!/usr/bin/env python3

import sys

file = sys.argv[1]
args = sys.argv[2:]

with open(file, "w") as f:
   i = 0
   while i < len(args):
      f.write(args[i] + "\n")
      i += 1
