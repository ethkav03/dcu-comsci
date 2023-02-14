#!/usr/bin/env python3

n = 10
smallest_even = int(input())

i = 0
while i + 1 < n:
   num = int(input())
   if num % 2 == 0 and num < smallest_even:
      smallest_even = num
   i += 1
print(smallest_even)
