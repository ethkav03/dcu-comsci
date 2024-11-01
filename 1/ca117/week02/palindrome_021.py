#!/usr/bin/env python3

import sys

def format_string(s):
    s = s.strip().lower()
    for char in s:
        if not char.isalpha() and not char.isdigit():
            s = s.replace(char, "")
    return s


for line in sys.stdin:
    s = format_string(line)
    print(s == s[::-1])
