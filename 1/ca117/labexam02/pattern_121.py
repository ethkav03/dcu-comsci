#!/usr/bin/env python3

import sys

def find_dashes(s):
  dashes = []
  i = 0
  while i < len(s):
    if pattern[i] == '-':
      dashes.append(i)
    i += 1
  return dashes

def add_dashes(s):
  for dash in dashes:
    s = s[:dash] + '-' + s[dash + 1:]
  return s


pattern = sys.stdin.readline().strip()

dashes = find_dashes(pattern)

words = []
lines = []
for line in sys.stdin:
  s = line.strip()
  lines.append(s)
  s = add_dashes(s)
  words.append(s)

matches = []
i = 0
while i < len(words):
  if words[i] == pattern:
    matches.append(lines[i])
  i += 1

if len(matches) > 0:
  print(', '.join(matches).strip(','))
