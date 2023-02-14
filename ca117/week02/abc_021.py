#!/usr/bin/env python3

import sys

d = {}

letters = ["A", "B", "C"]

numbers = sys.stdin.readline().strip()
lets = sys.stdin.readline().strip()

numbers = numbers.split()
numbs = []
i = 0
while i < len(numbers):
    numbs.append(int(numbers[i]))
    i += 1
numbs = sorted(numbs)
# print(numbs)

i = 0
for let in letters:
    d[let] = numbs[i]
    i += 1

s = ""
for let in lets:
    s += str(d[let]) + " "

print(s.strip())
