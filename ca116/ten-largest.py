#!/usr/bin/env python3

n = 10
largest = int(input())

i = 0
while i + 1 < n:
   num = int(input())
   if num > largest:
      largest = num
   i += 1
print(largest)
