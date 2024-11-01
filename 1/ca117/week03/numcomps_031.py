#!/usr/bin/env python3

import sys

def multiples_of_3(a):
    return [i for i in a if i % 3 == 0]

def multiples_of_3_squared(a):
    return [i * i for i in a if i % 3 == 0]

def multiples_of_4_doubled(a):
    return [i * 2 for i in a if i % 4 == 0]

def multiples_of_3_or_4(a):
    return [i for i in a if i % 3 == 0 or i % 4 == 0]

def multiples_of_3_and_4(a):
    return [i for i in a if i % 3 == 0 and i % 4 == 0]


for n in sys.stdin:
    a = range(1, int(n.strip()) + 1)
    print(f'Multiples of 3: {multiples_of_3(a)}')
    print(f'Multiples of 3 squared: {multiples_of_3_squared(a)}')
    print(f'Multiples of 4 doubled: {multiples_of_4_doubled(a)}')
    print(f'Multiples of 3 or 4: {multiples_of_3_or_4(a)}')
    print(f'Multiples of 3 and 4: {multiples_of_3_and_4(a)}')
