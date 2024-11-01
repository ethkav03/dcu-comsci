#!/usr/bin/env python3

import sys

args = int(sys.argv[1])

s = input()
a = []

j = 0
i = 0
while i < len(s):
   while j < len(s) and s[j] != ",":
      j += 1
   a.append(s[i:j])
   i = j + 1
   j += 1

print(a[args])
