#!/usr/bin/env python3

s = input()

weekday = ""

i = 0
while i < len(s) and s[i] != " ":
   i += 1

weekday = s[:i]

date = ""

j = i + 1
while j < len(s) and s[j] != " ":
   j += 1

date = s[i + 1:j]

month = ""

i = j + 1
while i < len(s) and s[i] != ",":
   i += 1

month = s[j + 1:i]

year = s[i + 2:]

print(month, date + ",", year, "(" + weekday + ")")
