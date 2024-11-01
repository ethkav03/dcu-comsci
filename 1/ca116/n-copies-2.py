#!/usr/bin/env python3

s = input()
n = int(input())

s = (s + "-") * n
print(s[:len(s) - 1])
