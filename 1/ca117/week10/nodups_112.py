#!/usr/bin/env python3

import sys
import string

def unpunctuate(s):
  return s.translate(str.maketrans('', '', string.punctuation))


words = {}

for line in sys.stdin:
  a = line.strip().split()
  line = ''
  for s in a:
    tmp = unpunctuate(s).lower()
    if tmp not in words:
      words[tmp] = 1
      line += f' {s}'
    else:
      line += ' .'
  print(line.strip())
