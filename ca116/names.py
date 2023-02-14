#!/usr/bin/env python3

import sys

d = {}

with open("boys.txt") as f:
   names = f.readlines()
   i = 0
   while i < len(names):
      d[names[i]] = "boy"
      i += 1

with open("girls.txt") as f:
   names = f.readlines()
   i = 0
   while i < len(names):
      if names[i] in d:
         d[names[i]] = "either"
      else:
         d[names[i]] = "girl"
      i += 1

names = sys.stdin.readlines()

i = 0
while i < len(names):
   if names[i] in d:
      print(names[i].strip(), d[names[i]])
   i += 1
