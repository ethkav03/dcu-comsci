#!/usr/bin/env python3

n = int(input())
p = int(input())

num = n // (10 ** (p + 1))
num2 = n - (num * (10 ** (p + 1)))
num3 = num2 // (10 ** p)

print(num3)
