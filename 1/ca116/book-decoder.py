#!/usr/bin/env python3

import sys

triplets = sys.stdin.readlines()
s = ""

i = 0
while i < len(triplets):
   coords = triplets[i].split()
   page = "page-" + coords[0] + ".txt"

   with open(page) as f:
      lines = f.readlines()
      s += lines[int(coords[1])][int(coords[2])]
   i += 1

print(s.strip())
