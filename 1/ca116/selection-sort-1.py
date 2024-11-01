#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

i = 0
p = i
if len(a) > 1:
   while i < len(a) - 1:
      if a[p] > a[i + 1]:
         p = i + 1
      i += 1

print(p)
