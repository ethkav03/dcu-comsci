#!/usr/bin/env python3

import sys

def vertical(a):
  verts = []
  try:
    for c in a[0]:
      verts.append(c)
    i = 0
    while i < len(a[0]):
      j = 1
      while j < len(a):
        verts[i] += a[j][i]
        j += 1
      i += 1
    return verts
  except IndexError:
    return []

def notalpha(a):
  for s in a:
    if not s.isalpha():
      return True

def main():
  a = sys.stdin.readlines()
  b = []
  for line in a:
    b.append(line.strip())
  if len(a) < 1:
    exit()
  length = len(a[0])
  for s in a:
    if len(s) != length:
      exit()

  if notalpha(b):
    return

  words = sorted(vertical(b), key=str.lower)

  if words == []:
    exit()

  vert_words = vertical(words)

  for s in vert_words:
    print(s)


if __name__ == '__main__':
  main()
