#!/usr/bin/env python3

n = int(input())

fib1 = 0
fib2 = 1

while fib1 + fib2 <= n:
   tmp = fib1
   fib1 = fib2
   fib2 = tmp + fib2

if n == 0 or fib2 == n:
   print("yes")
else:
   print("no")
