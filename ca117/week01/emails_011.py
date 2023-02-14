#!/usr/bin/env python3

import sys

first_name = ""
last_name = ""

for email in sys.stdin:
   email = email.strip()
   i = 0
   while i < len(email) and email[i] != '.':
      i += 1

   if i < len(email):
      first_name = email[:i]

   j = i
   while j < len(email) and email[j] != '@' and not email[j].isdigit():
      j += 1

   if i < len(email):
      last_name = email[i + 1:j]

   print(first_name.capitalize(), last_name.capitalize())
