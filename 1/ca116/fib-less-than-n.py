#!/usr/bin/env python3

n = int(input())

num1 = 0
num2 = 1

print(num1)
print(num2)

i = 0
while i < n:
   if num1 + num2 < n:
      print(num1 + num2)

   tmp = num1
   num1 = num2
   num2 = tmp + num2
   i = i + 1
