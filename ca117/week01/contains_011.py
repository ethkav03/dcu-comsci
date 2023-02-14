#!/usr/bin/env python3

import sys

for line in sys.stdin:
    s = line.strip()
    a = s.split()
    key = a[0].lower()
    string = a[1].lower()
    count = 0

    dupes = []
    for char in key:
        if key.count(char) > 1 and char not in dupes:
            dupes.append(char)
    if len(dupes) > 0:
        print("False")
    else:
        i = 0
        while i < len(key):
            j = 0
            while j < len(string) and key[i] != string[j]:
                j += 1

            if j < len(a[1]):
                count += 1
            i += 1

        if count == len(a[0]):
            print("True")
        else:
            print("False")
