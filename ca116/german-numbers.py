#!/usr/bin/env python3

import sys

german = "eins zwei drei vier funf sechs sieben acht neun zehn".split()
english = "one two three four five six seven eight nine ten".split()

d = {}

i = 0
while i < len(german):
   d[english[i]] = german[i]
   i += 1

word = sys.stdin.readline().strip()

while len(word) > 0:
   if word in d:
      print(d[word])

   word = sys.stdin.readline().strip()
