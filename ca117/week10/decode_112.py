#!/usr/bin/env python3

import sys

for line in sys.stdin:
  s = line.strip()
  i = 0
  while i < len(s):
    if s[i] in 'aeiou':
      s = s[:i + 1] + s[i + 3:]
    i += 1

  print(s)
