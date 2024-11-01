#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline())
buckets = sys.stdin.readline()

a = buckets.split()
filled = 0

i = 0
while i < len(a) and n > 0:
   n -= int(a[i])
   filled += 1
   i += 1

if n >= 0:
   print(filled)
else:
   print(filled - 1)
