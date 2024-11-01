#!/usr/bin/env python3

import sys

a = sys.stdin.readlines()

i = 0
while i < len(a):
   b = a[i].split("/")
   s = b[len(b) - 1]
   print(s.strip())
   i += 1
