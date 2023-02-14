#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

i = int(input())
p = i
while i < len(a) - 1:
   if a[p] > a[i + 1]:
      p = i + 1
   i += 1

print(p)
