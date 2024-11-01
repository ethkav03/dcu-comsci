#!/usr/bin/env python3

s = input()
a = []
b = []

while s != "end":
   a.append(s)
   s = input()

i = 0
while i < len(a):
   b = a[i].split(" ")
   print(b[3])
   i += 1
