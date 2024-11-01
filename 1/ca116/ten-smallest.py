#!/usr/bin/env python3

n = 10
smallest = int(input())

i = 0
while i + 1 < n:
   num = int(input())
   if num < smallest:
      smallest = num
   i += 1
print(smallest)
