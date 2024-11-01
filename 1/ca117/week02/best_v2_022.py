#!/usr/bin/env python3

import sys

file = sys.argv[1]
a = []

try:
    with open(file) as f:
        a = f.readlines()

    highscore = 0
    d = {}

    for line in a:
        line = line.strip().split()
        if line[0] not in d:
            d[line[0]] = " ".join(line[1:])
        if int(line[0]) > highscore:
            highscore = int(line[0])
    # print(d)

    print(f'Best student: {d[str(highscore)]}')
    print(f'Best mark: {highscore}')

except FileNotFoundError:
    print(f'The file {file} could not be opened.')
except ValueError:
    print(f'Invalid mark {line[0]} encountered. Exiting.')
