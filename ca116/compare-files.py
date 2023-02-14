#!/usr/bin/env python3

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f:
   a = f.read()

with open(file2) as f:
   b = f.read()

i = 0
pos = 0
line = 0
while i < len(a) and i < len(b) and a[i] == b[i]:
   if a[i] == "\n" and "\n":
      line += 1
   i += 1
   pos += 1

   if (i < len(a) or i < len(b)) and (a[i - 1] == "\n" or b[i - 1] == "\n"):
      pos = 0

if i < len(a) or i < len(b):
   print(line, pos)
