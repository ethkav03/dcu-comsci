#!/usr/bin/env python3

import sys

for line in sys.stdin:
  cakes = sorted(line.strip().split(), reverse=True)
  for i in range(0, len(cakes)):
    try:
      cakes[i] = int(cakes[i])
    except ValueError:
      break
  i = 0
  while i < len(cakes):
    if (i + 1) % 3 == 0:
      cakes.pop(i)
    i += 1
  try:
    print(sum(cakes))
  except ValueError:
    continue
