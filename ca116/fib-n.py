#!/usr/bin/env python3

n = int(input())

i = 0
num1 = 0
num2 = 1
print(i)
print(i + 1)
while i < n - 2:
   print(num1 + num2)
   tmp = num1
   num1 = num2
   num2 = tmp + num2
   i = i + 1
