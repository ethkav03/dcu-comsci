#!/usr/bin/env python3

import sys

hand = sys.stdin.readline().strip().split()

d = {}

for card in hand:
   if card[0] not in d:
      d[card[0]] = 1
   else:
      d[card[0]] += 1

print(max(d.values()))
