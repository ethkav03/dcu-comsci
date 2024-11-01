#!/usr/bin/env python3

import sys

file = sys.argv[1]
a = []


with open(file) as f:
    a = f.readlines()

highscore = 0
d = {}

for line in a:
    line = line.strip().split()
    mark = int(line[0])
    if mark > highscore:
        highscore = mark
    student = " ".join(line[1:])
    if student not in d:
        d[student] = mark

beststudents = "Best student(s): "

for key, value in d.items():
    if value == highscore:
        beststudents += key + ", "

print(beststudents[:-2])
print(f'Best mark: {highscore}')
