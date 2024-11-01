#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()
words = " ".join(words)

i = 0
while i < len(words) - 1:
   if words[i] == "." and words[i + 1] == " ":
      words = words[:i + 1] + "\n" + words[i + 2:]
   elif words[i] == "!" and words[i + 1] == " ":
      words = words[:i + 1] + "\n" + words[i + 2:]
   elif words[i] == "?" and words[i + 1] == " ":
      words = words[:i + 1] + "\n" + words[i + 2:]
   i += 1

words = words.split("\n")

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

i = 0
while i < len(words):
   j = 0
   while j < len(lower):
      if words[i][0] == lower[j]:
         words[i] = upper[j] + words[i][1:]
      j += 1
   print(words[i])
   i += 1
