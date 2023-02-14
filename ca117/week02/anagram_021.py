#!/usr/bin/env python3

import sys

for line in sys.stdin:
    [left, right] = line.strip().split()
    print("".join(sorted(left)) == "".join(sorted(right)))
