#!/usr/bin/env python3

import sys

def remove_lower(s):
   for c in s:
      if c.islower():
         s = s.replace(c, '-')
   return s.split('-')


for line in sys.stdin:
   s = line.strip()
   print(max(remove_lower(s), key=len))
