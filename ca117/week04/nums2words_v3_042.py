#!/usr/bin/env python3

import sys


d = {}
with open(sys.argv[1]) as f:
   lines = f.readlines()
   for line in lines:
      [key, value] = line.strip().split()
      d[key] = value

e = {
   '0': 'zero',
   '1': 'one',
   '2': 'two',
   '3': 'three',
   '4': 'four',
   '5': 'five',
   '6': 'six',
   '7': 'seven',
   '8': 'eight',
   '9': 'nine',
   '10': 'ten',
}

for line in sys.stdin:
   b = []
   a = line.strip().split()
   for num in a:
      b.append(d[e[num]])
   print(' '.join(b))
