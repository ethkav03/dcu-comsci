#!/usr/bin/env python3

import sys

def tagger(item):
   return item[1]


s = sys.stdin.read().lower()

d = {
   'a': 0,
   'e': 0,
   'i': 0,
   'o': 0,
   'u': 0,
}

for c in s:
   if c in 'aeiou':
      d[c] += 1

max = len(str(max(d.values())))

for key, value in sorted(d.items(), key=tagger, reverse=True):
   print(f'{key} : {value:>{max}}')
