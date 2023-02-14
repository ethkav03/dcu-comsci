#!/usr/bin/env python3

import sys

def seventeen_letters(a):
   return [s for s in a if len(s) == 17]

def eighteen_plus_letters(a):
   return [s for s in a if len(s) > 17]

def four_as(a):
   return [s for s in a if s.lower().count('a') == 4]

def two_plus_qs(a):
   return [s for s in a if s.lower().count('q') >= 2]

def contains_cie(a):
   return [s for s in a if s.lower().count('cie')]

def anagrams(a):
   return [s for s in a if "".join(sorted(s.lower())) == "aegln" and s != "angle"]


a = []
for s in sys.stdin:
   a.append(s.strip())

print(f'Words containing 17 letters: {seventeen_letters(a)}')
print(f'Words containing 18+ letters: {eighteen_plus_letters(a)}')
print(f"Words with 4 a's: {four_as(a)}")
print(f"Words with 2+ q's: {two_plus_qs(a)}")
print(f'Words containing cie: {contains_cie(a)}')
print(f'Anagrams of angle: {anagrams(a)}')
