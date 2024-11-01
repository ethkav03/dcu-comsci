#!/usr/bin/env python3

import sys

max_len = 0

a = sys.stdin.readlines()

for line in a:
   s = line.strip()
   if len(s) > max_len:
      max_len = len(s)

for line in a:
   s = line.strip()
   print(f'{s: ^{max_len}}')
