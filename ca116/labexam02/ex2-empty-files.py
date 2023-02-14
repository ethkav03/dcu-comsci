#!/usr/bin/env python3

import sys

args = sys.argv[1:]

i = 0
while i < len(args):
   with open(args[i]) as f:
      words = f.read()
      if len(words) == 0:
         print(args[i])
   i += 1
