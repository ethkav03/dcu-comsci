#!/usr/bin/env python3

import sys

n = int(input())

a = sys.stdin.readlines()

plot = [" "] * n

i = 0
while i < len(a):
   plot[int(a[i])] = "*"
   i += 1

print("|" + "".join(plot) + "|")
