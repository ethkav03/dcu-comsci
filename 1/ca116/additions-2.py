#!/usr/bin/env python3

s = input()

total = 0
i = 0
j = 0
k = 0
while i < len(s) and i < 4:
   while s[j] != "+":
      j += 1
   total += int(s[k:j])
   j += 1
   k = j
   i += 1

total += int(s[k:])

print(total)
