#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()

d = {}

i = 0
while i < len(words):
   if words[i] in d:
      d[words[i]] += 1
   else:
      d[words[i]] = 1
   i += 1

for word, count in d.items():
   if count == 1:
      print(word.strip())
