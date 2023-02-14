#!/usr/bin/env python3

s = input()
capLet = 0

i = 0
while i < len(s):
   if s[i] <= "Z" and s[i] >= "A":
      capLet += 1
   i += 1
print(capLet)
