#!/usr/bin/env python3

n = 10

i = 0
while i < n:
   s = input()
   j = 0
   while j < len(s) and s[j] != "+":
      j += 1
   num1 = int(s[:j])
   num2 = int(s[j + 1:])
   print(num1 + num2)
   i += 1
