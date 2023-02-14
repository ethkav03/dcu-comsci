#!/usr/bin/env python3

import sys

lotto = sys.argv[1:]

d = {
   "0": "0",
   "1": "1",
   "2": "5",
   "3": "100",
}

numbers = sys.stdin.readlines()

i = 0
while i < len(numbers):
   amount = 0
   a = numbers[i].split()
   j = 0
   while j < len(a):
      k = 0
      while k < len(lotto):
         if lotto[k] == a[j]:
            amount += 1
         k += 1
      j += 1
   print(d[str(amount)])
   i += 1
