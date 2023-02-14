#!/usr/bin/env python3

s = input()
t = ""

i = 0
while i < len(s):
   if s[i] != " ":
      t += s[i]
   i += 1
print(t)
