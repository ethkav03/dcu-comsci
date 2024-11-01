#!/usr/bin/env python3

f = input()

i = 0
while i < len(f) and not f[i] == ".":
   i += 1

if i == len(f):
   print(f + ".0")
elif i == len(f) - 1:
   print(f + "0")
elif i == 0:
   print("0" + f)
elif f[0] == "-" and f[1] == ".":
   print("-0" + f[1:])
else:
   print(f)
