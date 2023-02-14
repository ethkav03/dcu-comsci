#!/usr/bin/env python3

n = int(input())
m = n // 2

i = 0
while i < n - 1:
   print((" " * (i // 2)) + "*" + (" " * (n - i - 2)) + "*")
   i += 2

print(" " * m + "*")

i = 0
while i < n - 1:
   print((" " * ((m - i // 2) - 1)) + "*" + (" " * (i + 1)) + "*")
   i += 2
