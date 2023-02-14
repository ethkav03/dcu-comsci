#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

i = 0
while i < len(a):
   j = i + 1
   while j < len(a):
      if a[j] < a[i]:
         tmp = a[j]
         a[j] = a[i]
         a[i] = tmp
      j += 1
   i += 1

print(a[len(a) // 2])
