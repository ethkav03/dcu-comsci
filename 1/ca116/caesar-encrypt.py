#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

d = {}

i = 0
while i < len(lower):
   d[lower[i]] = lower[(i + n) % 26]
   i += 1

i = 0
while i < len(upper):
   d[upper[i]] = upper[(i + n) % 26]
   i += 1

words = sys.stdin.read()
s = ""

i = 0
while i < len(words):
   if words[i] in d:
      s += d[words[i]]
   else:
      s += words[i]
   i += 1

print(s.strip())
