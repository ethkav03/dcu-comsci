#!/usr/bin/env python3

n = int(input())

start = n // 10000
end = n // 100

final = end - (start * 100)

print(final)
