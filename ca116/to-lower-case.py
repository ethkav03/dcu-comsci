#!/usr/bin/env python3

s = input()

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while s != "end":
   i = 0
   while i < len(s):
      j = 0
      while j < len(upper):
         if s[i] == upper[j]:
            s = s[:i] + lower[j] + s[i + 1:]
         j += 1
      i += 1
   print(s)
   s = input()
i += 1
