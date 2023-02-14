#!/usr/bin/env python3

a = []

with open("irish-dobs.txt") as f_in:
   a = f_in.readlines()

i = 0
while i < len(a):
   b = a[i].split()
   c = b[0].split("/")
   tmp = c[0]
   c[0] = c[1]
   c[1] = tmp
   b[0] = "/".join(c)
   a[i] = " ".join(b)
   i += 1

with open("american-dobs.txt", "w") as f_out:
   i = 0
   while i < len(a):
      f_out.write(a[i] + "\n")
      i += 1
