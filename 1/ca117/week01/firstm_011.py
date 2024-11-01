#!/usr/bin/env python3

import sys

for line in sys.stdin:
    s = line.strip()

    i = 0
    while i < len(s) and s[i] != "m":
        i += 1

    if i < len(s):
        print(s[:i] + s[i].upper() + s[i + 1:])
    else:
        print(s)
