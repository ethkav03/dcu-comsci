#!/usr/bin/env python3

import sys

def tagger(item):
   return item[1]


a = sys.stdin.readlines()

d = {}

for line in a:
   [name, sales] = line.strip().split(':')
   sales = sales.split()
   total = 0
   for sale in sales:
      n = int(sale.strip(','))
      total += n

   d[name] = total / len(sales)

b = sorted(d.items(), key=tagger, reverse=True)

for s in b:
   print(f'{s[0]}: {s[1]:.2f}')
