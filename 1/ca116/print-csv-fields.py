#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(s)
   s = input()

n = int(input())

i = 0
while i < len(a):
   j = 0
   while j < len(a[i]) and a[i][j] != ",":
      j += 1
   k = j + 1
   while k < len(a[i]) and a[i][k] != ",":
      k += 1

   if n == 0:
      print(a[i][:j])
   elif n == 1:
      print(a[i][j + 1:k])
   else:
      print(a[i][k + 1:])
   i += 1
