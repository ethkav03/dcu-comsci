#!/usr/bin/env python3

s = input()

a = []

while s != "end":
   a.append(int(s))
   s = input()

n = int(input())

i = 0
while i < len(a):
   print(a[i] + n)
   i += 1
