#!/usr/bin/env python3

n = 10
smallest_positive = int(input())

i = 0
while i + 1 < n:
   num = int(input())
   if num > 0 and num < smallest_positive:
      smallest_positive = num
   i += 1
print(smallest_positive)
