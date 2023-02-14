#!/usr/bin/env python3

import sys

def tagger(item):
   return item[1]


a = sys.stdin.readlines()

d = {}
dis = []
for line in a:
   s = line.strip().split()
   try:
      d[' '.join(s[:-3])] = int(s[-3]) + int(s[-2]) + int(s[-1])
   except ValueError:
      dis.append(' '.join(s[:-3]))

scores = []
for k, v in sorted(d.items(), key=tagger):
   print(f'{k}: {v}')

if len(dis) > 0:
   print(f'Disqualified: {", ".join(dis)}')
