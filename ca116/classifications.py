#!/usr/bin/env python3

n = int(input())

print('first: ' + str(n >= 70))
print('second: ' + str(n <= 69 and n >= 50))
print('third: ' + str(n <= 49 and n >= 40))
print('fail: ' + str(n < 40))
