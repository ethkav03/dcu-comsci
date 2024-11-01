#!/usr/bin/env python3

n = 5

prev = int(input())
curr = 0

i = 0
while i < n:
   curr = int(input())
   if curr == prev:
      print("equal")
   elif curr < prev:
      print("lower")
   else:
      print("higher")
   prev = curr
   i += 1
