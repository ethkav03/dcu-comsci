#!/usr/bin/env python3

import sys

n = 20

coords = sys.stdin.readlines()

print(" " + "-" * 20)

s = ""

i = 0
while i < n:
   a = [" "] * 20

   k = 0
   while k < len(coords):
      b = coords[k].split()
      if 19 - int(b[1]) == i:
         a[int(b[0])] = "*"
      k += 1

   j = 0
   while j < len(a):
      s += a[j]
      j += 1
   print("|" + s + "|")
   i += 1
   s = ""

print(" " + "-" * 20)
