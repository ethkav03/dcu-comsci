#!/usr/bin/env python3

import sys

N = int(sys.stdin.readline().strip())
s = sys.stdin.readline()

buckets = s.strip().split()

filled = 0
litres = 0
for bucket in buckets:
   litres += int(bucket)
   if litres < N:
      filled += 1

print(filled)
