#!/usr/bin/env python3

import sys

d = {}

words = sys.stdin.readlines()

i = 0
while i < len(words):
   a = words[i].split(".")
   d[a[0] + "." + a[1]] = a[2].strip()
   i += 1

e = {}

for file, correct in d.items():
   user = file.split("/")
   user = user[0]
   if user not in e:
      e[user] = 0
   if correct == "correct":
      e[user] += 1

for key, value in e.items():
   print(key, value)
