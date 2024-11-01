#1?usr/bin/env python3

import sys

def format_string(s):
   for c in s:
      if not c.isalpha():
         s = s.replace(c, '')
   return s

def not_in(s):
   non = []
   for c in alpha:
      if c not in s:
         non.append(c)
   return non


alpha = 'abcdefghijklmnopqrstuvwxyz'

for line in sys.stdin:
   s = line.strip().lower()
   s = format_string(s)
   non = not_in(s)

   if len(non) == 0:
      print('pangram')
   else:
      print(f'missing {"".join(non)}')
