#!/usr/bin/env python3

import sys

def classes(password, digit, upper, lower, other):
    amount = 0

    for c in password:
        if c.isdigit():
            digit = True
        elif c.isupper():
            upper = True
        elif c.islower():
            lower = True
        else:
            other = True

    if digit:
        amount += 1
    if lower:
        amount += 1
    if upper:
        amount += 1
    if other:
        amount += 1

    return amount


for line in sys.stdin:
    upper = False
    lower = False
    digit = False
    other = False

    s = line.strip()

    print(classes(s, digit, upper, lower, other))
