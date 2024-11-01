#!/usr/bin/env python3

n = int(input())

hex = "0123456789abcdef"
t = ""

i = 0
while n // (16 ** i) > 15:
   i += 1

while i >= 0:
   #print(n, "//", 16 ** i, "=", n // (16 ** i))
   #print(n // (16 ** i))
   #print(hex[n // (16 ** i)])
   t += hex[n // (16 ** i)]
   #print("i:", i)
   #print((16 ** i) * (n // (16 ** 1)))
   if n // (16 ** i) < 16 and n // (16 ** i) > 0:
      n -= (16 ** i) * (n // (16 ** i))
   i -= 1
print(t)
