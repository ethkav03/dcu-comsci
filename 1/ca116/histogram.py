#!/usr/bin/env python3

n = 10

s = input()

a = []

while s != "end":
   a.append(int(s))
   s = input()

i = 0
while i < n:
   tmp = 0
   j = 0
   while j < len(a):
      if i == a[j]:
         tmp += 1
      j += 1
   print(i, "*" * tmp)
   i += 1
