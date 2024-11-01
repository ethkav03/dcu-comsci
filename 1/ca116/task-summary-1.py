#!/usr/bin/env python3

import sys

results = sys.stdin.readlines()

d = {}

i = 0
while i < len(results):
   a = results[i].split(".")
   d[a[0] + "." + a[1]] = a[2].strip()
   i += 1

for file, correct in d.items():
   if correct == "correct":
      print(file)
