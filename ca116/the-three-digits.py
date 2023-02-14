#!/usr/bin/env python3

n = int(input())

a = n // 100
b = (n // 10) - (a * 10)
c = n - ((a * 100) + (b * 10))
print(a)
print(b)
print(c)
