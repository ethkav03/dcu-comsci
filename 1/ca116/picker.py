#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input()) - 1

print((a * (c % 2)) + b * (1 - (c % 2)))
