#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(s)
   s = input()

i = 0
while i < len(a):
   if a[i][0] == "3":
      print(a[i])
   i += 1
