#!/usr/bin/env python3

import sys

def replace_with_x(a):
   return ['X' if int(n) % 3 == 0 else n for n in a]


for n in sys.stdin:
   a = range(1, int(n.strip()) + 1)
   print(f'Multiples of 3 replaced: {replace_with_x(a)}')
