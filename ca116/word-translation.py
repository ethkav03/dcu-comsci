#!/usr/bin/env python3

import sys

with open("translation.txt") as f:
   words = f.readlines()

d = {}

i = 0
while i < len(words):
   b = words[i].split()
   d[b[0]] = b[1]
   i += 1

word = sys.stdin.readline().strip()

while len(word) > 0:
   if word in d:
      print(d[word])

   word = sys.stdin.readline().strip()
