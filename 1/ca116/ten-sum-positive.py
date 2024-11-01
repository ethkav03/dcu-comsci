#!/usr/bin/env python3

n = 10
sum = 0

i = 0
while i < n:
   num = int(input())
   if num >= 0:
      sum += num
   i += 1
print(sum)
