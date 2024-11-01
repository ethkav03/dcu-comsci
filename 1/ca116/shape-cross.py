#!/usr/bin/env python3

n = int(input())
m = n // 2

i = 0
while i < n:
   if i == m:
      print("*" * n)
   else:
      print((" " * m) + "*")
   i += 1
