#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(s)
   s = input()

i = 0
while i < len(a):
   p = i + 1
   while p < len(a):
      if a[p] < a[i]:
         tmp = a[p]
         a[p] = a[i]
         a[i] = tmp
      p += 1
   i += 1

i = 0
while i < len(a):
   print(a[i])
   i += 1
