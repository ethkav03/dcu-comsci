#!/usr/bin/env python3

import sys

d = {
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
      if num in d:
         b.append(d[num])
      else:
         b.append('unknown')
   print(' '.join(b))
