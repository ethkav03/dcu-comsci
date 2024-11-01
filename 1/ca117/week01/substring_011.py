#!/usr/bin/env python3

import sys

for line in sys.stdin:
    s = line.strip()
    a = s.split()
    key = a[0].lower()
    string = a[1].lower()

    if string.__contains__(key):
        print("True")
    else:
        print("False")
