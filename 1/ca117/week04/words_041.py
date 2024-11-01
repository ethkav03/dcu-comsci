#!/usr/bin/env python3

import sys

def reformat(s):
   for c in s:
      if c == '\n':
         s = s.replace(c, ' ')
      elif not c.isalpha() and c != "'" and c != ' ':
         s = s.replace(c, '')
   return s


s = sys.stdin.read()
s = s.lower()
s = reformat(s)

a = s.split()

d = {}

for s in a:
   if s not in d:
      d[s] = 1
   else:
      d[s] += 1

for name, value in sorted(d.items()):
   print(f'{name} : {value}')
