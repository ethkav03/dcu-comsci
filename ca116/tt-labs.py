#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(s)
   s = input()

b = []

i = 0
while i < len(a):
   b = a[i].split()
   if int(b[2]) > 1:
      print(a[i])
   i += 1
