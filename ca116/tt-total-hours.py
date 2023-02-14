#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(s)
   s = input()

b = []
hours = 0

i = 0
while i < len(a):
   b = a[i].split()
   hours += int(b[2])
   i += 1

print(hours)
