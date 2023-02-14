#!/usr/bin/env python3

import sys

def isprime(n):
   if n <= 1:
      return False

   for i in range(2, n // 2 + 1):
      if n % i == 0:
         return False
   return True


for n in sys.stdin:
   print(f'Primes: {[i for i in range(2, int(n)) if isprime(i)]}')
