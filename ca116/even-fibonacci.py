#!/usr/bin/env python3

import sys

n = sys.argv[1]
n = int(n)

total = 0

num1 = 0
num2 = 1

while num1 + num2 < n:
   tmp = num1
   num1 = num2
   num2 += tmp

   if num2 % 2 == 0:
      total += num2

print(total)
