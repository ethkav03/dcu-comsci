#!/usr/bin/env python3

import sys

message = sys.stdin.read().strip()
triplets = [""]
letter = False

i = 0
while i < len(message):
   letter = False
   j = 0
   while j < 10 and not letter:
      page = "page-" + str(j) + ".txt"
      with open(page) as f:
         lines = f.readlines()
         k = 0
         while k < len(lines) and not letter:
            l = 0
            while l < len(lines[k]) and message[i] != lines[k][l]:
               l += 1
            if l < len(lines[k]):
                  letter = True
            k += 1
      j += 1
      m = 0
      while m < len(triplets) and str(j - 1) + " " + str(k - 1) + " " + str(l - 1) != triplets[m]:
         m += 1

      if m == len(triplets):
         triplets.append(str(j - 1) + " " + str(k - 1) + " " + str(l - 1))
      else:
         letter = False
   i += 1

i = 0
while i + 1 < len(triplets):
   print(triplets[i + 1])
   i += 1
