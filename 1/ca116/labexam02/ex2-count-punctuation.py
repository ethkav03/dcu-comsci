#!/usr/bin/env python3

import sys

text = sys.stdin.read()

total = 0

d = {
   "!": 1,
   ".": 1,
   ",": 1,
   "?": 1,
   ";": 1,
   ":": 1,
}

i = 0
while i < len(text):
   if text[i] in d:
      total += 1
   i += 1

print(total)
