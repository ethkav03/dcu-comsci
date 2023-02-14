#!/usr/bin/env python3

import sys

args = sys.argv[1]

i = 0
while i < len(args) and args[i] != "=":
   i += 1

header = args[:i]
value = args[i + 1:]
pos = 0

s = input()
a = []

i = 0
j = 0
if s != "end":
   while i < len(s):
      while j < len(s) and s[j] != ",":
         j += 1
      a.append(s[i:j])
      i = j + 1
      j += 1

i = 0
while i < len(a):
   if a[i] == header:
      pos = i
   i += 1

a = []
s = input()

while s != "end":
   i = 0
   j = 0
   while i < len(s):
      while j < len(s) and s[j] != ",":
         j += 1
      a.append(s[i:j])
      i = j + 1
      j += 1

   if a[pos] == value:
      s = a[0]
      i = 1
      while i < len(a):
         s += "," + a[i]
         i += 1
      print(s)

   a = []
   s = input()
