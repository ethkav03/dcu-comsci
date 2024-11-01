#!/usr/bin/env python3

s = input()
a = []
dob = []

while s != "end":
   a.append(s)
   s = input()

i = 0
while i < len(a):
   j = i + 1
   while j < len(a):
      if a[i][6:8] > a[j][6:8]:
         tmp = a[i]
         a[i] = a[j]
         a[j] = tmp
      j += 1
   i += 1

i = 0
while i < len(a):
   j = i + 1
   while j < len(a):
      if a[i][6:8] == a[j][6:8]:
         if a[i][3:5] > a[j][3:5]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
      j += 1
   i += 1

i = 0
while i < len(a):
   j = i + 1
   while j < len(a):
      if a[i][6:8] == a[j][6:8] and a[i][3:5] == a[j][3:5]:
         if a[i][:2] > a[j][:2]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
      j += 1
   i += 1


i = 0
while i < len(a):
   print(a[i][9:])
   i += 1
