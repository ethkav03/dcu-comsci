#!/usr/bin/env python3

import sys

def definition(a, d):
    #checks for correct amount of arguments
   try:
      [name, val] = a
   except ValueError:
      return 'error'
    #checks that 'val' is a valid integer
   try:
      val = int(val)
   except ValueError:
      return 'error'
    #checks for value with in range -1000 to 1000
   if val > 1000 or val < -1000:
      return 'error'
    #checks for name length of 1 to 30
   if len(name) > 30 or len(name) < 0:
      return 'error'
    #checks name is not 'unknown', name is all alphabetical and lowercase
   if name == 'unknown' or not name.isalpha() or not name.islower():
      return 'error'
    #checks if value is already stored in another variable
   for v in d.values():
      if v == val:
         return 'error'

    #adds new variable and value to dictionary
   d[name] = val
   return d

def calculation(a, d):
    #checks that list 'a' is not empty
   if len(a) < 1:
      return 'error'
    #checks that '=' is present and atleast one of '-' or '+' is present
   if '=' not in a:
      return 'error'
   try:
      total = d[a[0]]
   except KeyError:
      return 'unknown'
   i = 1
   while i < len(a):
      if a[i] == '+':
         try:
            #adds to total
            total += d[a[i + 1]]
            i += 1
         except KeyError:
            return 'unknown'
      elif a[i] == '-':
         try:
            #subtracts from total
            total -= d[a[i + 1]]
            i += 1
         except KeyError:
            return 'unknown'
      i += 1

    #checks for a variable name with a value equal to total
   for k, v in d.items():
      if v == total:
         return k
   return 'unknown'


d = {}
count = 0
for line in sys.stdin:
   if count < 1000:
      a = line.strip().split()
      com = a[0]
      a = a[1:]
      if com == 'def':
         defin = definition(a, d)
      elif com == 'calc':
         calc = calculation(a, d)
        #prints equation only if no error was returned
         if calc != 'error':
            print(' '.join(a), calc)
      elif com == 'clear':
         d = {}
      else:
         print('Invalid Command')
      count += 1
   else:
      exit()
