#!/usr/bin/env python3

s = input()

a = [0] * 1000
b = [""] * 1000

while s != "end":
   b[int(s)] = int(s)
   a[int(s)] += 1
   s = input()

i = 0
while i < len(b):
   if a[i] > 0 and a[i] != "":
      print(b[i])
      a[i] -= 1
   else:
      i += 1
