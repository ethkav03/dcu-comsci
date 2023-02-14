#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
   lines = f.readlines()

contacts = {}

for line in lines:
   [name, number] = line.strip().split()
   contacts[name] = number

for name in sys.stdin:
   name = name.strip()
   print(f'Name: {name}')
   try:
      print(f'Phone: {contacts[name]}')
   except KeyError:
      print('No such contact')
