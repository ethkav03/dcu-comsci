#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

d = {}

i = 0
while i < len(src):
   d[dst[i]] = src[i]
   i += 1

words = sys.stdin.read()

s = ""

i = 0
while i < len(words):
   if words[i] in d:
      s += d[words[i]]
   else:
      s += words[i]
   i += 1

print(s.strip())
