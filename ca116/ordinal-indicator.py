#!/usr/bin/env python3

n = int(input())

pos = n % 10

if n % 100 == 11:
   print("th")
elif n % 100 == 12:
   print("th")
elif n % 100 == 13:
   print("th")
elif pos == 1:
   print("st")
elif pos == 2:
   print("nd")
elif pos == 3:
   print("rd")
else:
   print("th")
