#!/usr/bin/env python3

import sys

d = {}
counter = 1

with open("a.txt") as f:
   words = f.readlines()
   i = 0
   while i < len(words):
      d[words[i]] = 1
      i += 1

with open("b.txt") as f:
   words = f.readlines()
   i = 0
   while i < len(words) and words[i] not in d:
      i += 1

if i == len(words):
   print("disjoint")
else:
   print("intersecting")
