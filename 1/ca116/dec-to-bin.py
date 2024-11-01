#!/usr/bin/env python3

n = int(input())
t = ""

i = 0
while n // (2 ** i) != 1:
   i += 1

while i >= 0:
   t += str(n // (2 ** i))
   #print(n, "//", 2 ** i, "=", n // (2 ** i))
   #print(i)
   if n // (2 ** i) == 1:
      n -= (2 ** i)
   i -= 1
print(t)
