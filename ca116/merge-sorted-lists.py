#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

s = input()
b = []
while s != "end":
   b.append(int(s))
   s = input()

c = []

i = 0
j = 0
while i < len(a) and j < len(b):
   if a[i] > b[j]:
      c.append(b[j])
      j += 1
   elif a[i] < b[j]:
      c.append(a[i])
      i += 1
   else:
      c.append(a[i])
      c.append(b[j])
      i += 1
      j += 1

while i < len(a):
   c.append(a[i])
   i += 1

while j < len(b):
   c.append(b[j])
   j += 1

i = 0
while i < len(c):
   print(c[i])
   i += 1
