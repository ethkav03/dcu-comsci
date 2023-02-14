#!/usr/bin/env python3

import sys

letters = []

with open("input.txt") as f_in:
   lines = f_in.readlines()
   i = 0
   while i < len(lines):
      s = ""
      j = 0
      while j < len(lines[i]):
         if lines[i][j] >= "A" and lines[i][j] <= "Z":
            s += "*"
         elif lines[i][j] >= "a" and lines[i][j] <= "z":
            s += "*"
         else:
            s += lines[i][j]
         j += 1
      lines[i] = s.strip()
      i += 1

with open("output.txt", "w") as f_out:
   i = 0
   while i < len(lines):
      f_out.write(lines[i] + "\n")
      i += 1
