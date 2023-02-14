#!/usr/bin/env python3

import sys

d = {}

counter = 1

words = sys.stdin.readlines()

i = 0
while i < len(words) and counter != 2:
   if words[i] in d:
      counter += 1
      if counter == 2:
         print("snap:", words[i].strip())
   else:
      d[words[i]] = 1

   i += 1
