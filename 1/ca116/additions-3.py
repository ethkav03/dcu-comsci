#!/usr/bin/env python3

s = input()
n = 1

while n == 1:
   j = 0
   while j < len(s) and s[j] != "+":
      j += 1
   num1 = int(s[:j])
   num2 = int(s[j + 1:])
   print(num1 + num2)

   if num1 + num2 == 1000:
      n = 0
   else:
      s = input()
