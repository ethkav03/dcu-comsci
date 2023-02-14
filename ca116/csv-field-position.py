#!/usr/bin/env python3

import sys

args = sys.argv[1]

s = input()
a = []

i = 0
j = 0
while i < len(s):
   while j < len(s) and s[j] != ",":
      j += 1
   i += 1
   a.append(s[i - 1:j])
   i = j + 1
   j += 1

i = 0
while i < len(a):
   if a[i] == args:
      print(i)
   i += 1
