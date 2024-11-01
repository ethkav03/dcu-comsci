#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(s)
   s = input()

b = []

if len(a) > 0:
   b.append(a[0])

   i = 0
   while i < len(a):
      j = 0
      while j < len(b) and a[i] != b[j]:
         j += 1

      if j == len(b):
         b.append(a[i])
      i += 1

   i = 0
   while i < len(b):
      print(b[i])
      i += 1
