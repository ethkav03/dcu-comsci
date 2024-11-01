#!/usr/bin/env python3

import sys

d = {}

with open("a.txt") as f:
   words = f.readlines()
   i = 0
   while i < len(words):
      d[words[i]] = 1
      i += 1

with open("b.txt") as f:
   words = f.readlines()
   i = 0
   while i < len(words):
      d[words[i]] = 1
      i += 1

for word in d:
   print(word.strip())
