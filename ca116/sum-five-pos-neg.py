#!/usr/bin/env python3

n = 5

pos = 0
neg = 0

i = 0
while i < n:
   num = int(input())
   if num < 0:
      neg += num
   else:
      pos += num
   i += 1
print(neg, pos)
