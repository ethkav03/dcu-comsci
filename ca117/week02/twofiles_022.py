#!/usr/bin/env python3

from re import A
import sys

args = sys.argv[1:]
[file1, file2] = args

a = []

with open(file1) as f1:
    with open(file2) as f2:
        b = f1.readlines()
        c = f2.readlines()

i = 0
while i < len(b):
    a.append(b[i])
    a.append(c[i])
    i += 1

for c in a:
    print(c.strip())
