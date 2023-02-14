#!/usr/bin/env python3

import sys
args = sys.argv[1:]

i = 0
while i < len(args):
   path = []
   components = args[i].split("/")
   head = components[0]
   components = components[1:]

   j = 0
   while j < len(components):
      if components[j] == ".." and 0 < len(path):
         path.pop()
      elif components[j] == ".." or components[j] == ".":
         pass
      else:
         path.append(components[j])
      j = j + 1
   print(head + "/" + "/".join(path))
   i = i + 1
