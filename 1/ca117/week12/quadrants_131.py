#!/usr/bin/env python3

import sys

def findQuadrant(x, y):
  try:
    if int(x) > 0:
      if int(y) > 0:
        return 1
      else:
        return 2
    else:
      if int(y) > 0:
        return 4
      else:
        return 3
  except ValueError:
    return None


for line in sys.stdin:
  try:
    [x, y] = line.strip().split()
  except ValueError:
    continue
  quad = findQuadrant(x, y)
  if quad is not None:
    print(quad)
