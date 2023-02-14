#!/usr/bin/env python3

import sys

def same_reverse(q):
   low = 0
   high = len(a)
   while low < high:
      mid = (low + high) // 2
      if a[mid].lower() < q:
         low = mid + 1
      else:
         high = mid
   return a[low].lower() == q


a = []
for word in sys.stdin:
   s = word.strip()
   if len(s) >= 5:
      a.append(s)

print([s for s in a if same_reverse(s[::-1].lower())])
