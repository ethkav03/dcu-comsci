#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
   print(i * (((i + 1) % 2) + ((i + 1) % 2) - 1))
   i = i + 1
