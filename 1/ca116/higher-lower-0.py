#!/usr/bin/env python3

prev = int(input())
if prev != 0:
   curr = int(input())

   while curr != 0:
      if curr == prev:
         print("equal")
      elif prev > curr:
         print("lower")
      else:
         print("higher")
      prev = curr
      curr = int(input())
