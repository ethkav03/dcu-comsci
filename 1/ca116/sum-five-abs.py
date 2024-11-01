#!/usr/bin/env python3

n = 5
total = 0

i = 0
while i < n:
   num = int(input())
   if num < 0:
      num = num * -1
   total += num
   i += 1
print(total)
