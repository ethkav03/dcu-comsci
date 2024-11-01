#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(s)
   s = input()

b = " ".join(a)

a = b.split()

b = " ".join(a)

i = 0
j = 0
while i < len(b):
   while j < len(b) and b[j] != ".":
      j += 1
   s = b[i:j + 1]
   print(s.lstrip())
   i = j + 1
   j += 1
