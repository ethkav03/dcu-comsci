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
   hours = int(b[2])
   b[1] = str(int(b[1]))
   b[2] = str(int(b[1]) + hours - 1)
   b[1] += ":00"
   b[2] += ":50"
   print(" ".join(b))
   i += 1
