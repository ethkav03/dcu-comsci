#!/usr/bin/env python3

s = input()
total = 0

i = 0
while i < len(s):
   total += int(s[i]) * (2 ** (len(s) - i - 1))
   i += 1
print(total)
