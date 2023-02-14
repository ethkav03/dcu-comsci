#!/usr/bin/env python3

s = input()

a = []

while s != "end":
   a.append(int(s))
   s = input()

i = 0
while i < len(a):
   if a[i] % 2 == 0:
      print(a[i])
   i += 1

i = 0
while i < len(a):
   if a[i] % 2 == 1:
      print(a[i])
   i += 1
