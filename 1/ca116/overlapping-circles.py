#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
t1 = int(input())

x2 = int(input())
y2 = int(input())
t2 = int(input())

cenLen = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)

if cenLen < (t1 + t2) ** 2:
   print("yes")
else:
   print("no")
