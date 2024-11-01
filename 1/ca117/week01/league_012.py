#!/usr/bin/env python3

import sys

a = sys.stdin.readlines()

max_len = 0
names = []

for line in a:
    line = line.strip().split()
    names.append(" ".join(line[1:-8]))

for name in names:
    if len(name) > max_len:
        max_len = len(name)

print("POS CLUB" + " " * (max_len - 3) + " P   W   D   L  GF  GA  GD PTS")

i = 0
for line in a:
    line = line.strip().split()
    print(f'{line[0]:>3s} {names[i]:<{max_len}s} {line[-8]:>2s} {line[-7]:>3s} {line[-6]:>3s} {line[-5]:>3s} {line[-4]:>3s} {line[-3]:>3s} {line[-2]:>3s} {line[-1]:>3s}')
    i += 1
