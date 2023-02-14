#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   j = 0
   while j < len(lines[i]) and lines[i][j] != "(":
      j += 1
   k = j + 1
   while k < len(lines[i]) and lines[i][k] != ")":
      k += 1

   if j < len(lines[i]) and k < len(lines[i]):
      print(lines[i][j + 1:k])
   i += 1
