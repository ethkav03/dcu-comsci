#!/usr/bin/env python3

import sys

def censor(censor, a):
   b = []
   for line in a:
      line = line.strip()
      b.append(line.replace(censor, '@' * len(censor)))
   return b


a = sys.stdin.readlines()

censors = a
with open(sys.argv[1]) as f:
   cs = f.readlines()
   for s in cs:
      s = s.strip()
      censors = censor(s, censors)

print("\n".join(censors))
