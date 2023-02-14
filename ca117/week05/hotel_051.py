#!/usr/bin/env python3

import sys

def create_range(a):
   x = []
   for n in a:
      x.append(n)
   return x

def available_rooms(a, rooms):
   b = []
   for n in a:
      if str(n) not in rooms:
         b.append(n)
   return b


nums = sys.stdin.readline().strip().split()

amount = nums[0]
rooms = nums[1:]

ran = range(1, int(amount))
x = create_range(ran)

available = available_rooms(x, rooms)

#print(rooms)
#print(ran)
#print(x)
#print(available)

if len(available) == 0:
   print('no room')
else:
   print(min(available))
