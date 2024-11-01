#!/usr/bin/env python3

months = int(input())
day = int(input())

total_days = (months * 30) - 30 + day
total_days -= 1
print((total_days % 7) + 1)
