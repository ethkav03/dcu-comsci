#!/usr/bin/env python3

n = int(input())
m = int(input())

num = m
print(m)

i = 0
while i < n - 1:
   if num % 2 == 0:
      num = num // 2
   else:
      num = (3 * num) + 1

   print(num)
   i = i + 1
