#!/usr/bin/env python3

import sys

def is_nice(s):
   a = []
   for c in s:
      if c in nice:
         a.append(c)
   return ''.join(a) == nice


nice = 'nice'
for line in sys.stdin:
   s = line.strip()
   if is_nice(s):
      print(s)
