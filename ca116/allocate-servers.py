#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

b = [0] * len(a)

i = 0
while i < len(a):
   j = i + 1
   while j < len(a):
      if int(a[j]) - int(a[i]) < 1000:
         b[i] += 1
      j += 1
   i += 1

i = 0
while i < len(a):
   j = i + 1
   while j < len(a):
      if b[i] < b[j]:
         tmp = b[i]
         b[i] = b[j]
         b[j] = b[i]
      j += 1
   i += 1

if len(a) > 0:
   print(b[0] + 1)
else:
   print("0")
