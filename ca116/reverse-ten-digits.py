#!/usr/bin/env python3

n = 10
num = 0

i = 0
while i < n:
   num += int(input()) * (10 ** i)
   i += 1

i = 0
while i < n:
   reverse = (num % (10 ** (n - i))) // (10 ** (n - (i + 1)))
   print(reverse)
   i += 1
