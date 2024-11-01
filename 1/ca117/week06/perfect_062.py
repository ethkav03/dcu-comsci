#!/usr/bin/env python4

import sys

def sum_factors(n):
   a = []
   i = 1
   while i * i <= n:
      if n % i == 0:
         a.append(i)
         if n // i != i:
            a.append(n // i)
      i += 1
   factors = sorted(a)

   total = 0
   for num in factors[:-1]:
      total += num

   return total

def is_perfect(factors, num):
   return factors == num


for line in sys.stdin:
   try:
      n = int(line.strip())
   except ValueError:
      print('Invalid Integer')
      continue
   sum_of_factors = sum_factors(n)

   print(is_perfect(sum_of_factors, n))
