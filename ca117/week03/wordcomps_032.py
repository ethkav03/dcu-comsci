#!/usr/bin/env python3

import sys

def shortest_vowels(a):
   return [s for s in a if contains_vowels(s.lower())]

def contains_vowels(s):
   return 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s

def ending_iary(a):
   return [s for s in a if s[-4:] == 'iary']

def most_es(a):
   most = 0
   for s in a:
      if s.lower().count('e') > most:
         most = s.lower().count('e')

   return [s for s in a if s.lower().count('e') == most]


a = []
for word in sys.stdin:
   s = word.strip()
   a.append(s)

print(f'Shortest word containing all vowels: {min(shortest_vowels(a), key=len)}')
print(f'Words ending in iary: {len(ending_iary(a))}')
print(f"Words with most e's: {most_es(a)}")
