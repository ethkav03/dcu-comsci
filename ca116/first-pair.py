#!/usr/bin/env python3

s = input()

if len(s) >= 2:
   i = 0
   while i + 1 < len(s) and not (s[i + 1] == s[i]):
      i += 1

   if i < len(s) - 1:
      print(s[i] + s[i + 1])
