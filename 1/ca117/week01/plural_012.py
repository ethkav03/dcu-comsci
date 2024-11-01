#!/usr/bin/env python3

import sys

def pluralize(word):
    if word[-2:] in ("ch", "sh") or word[-1] in ("x", "s", "z", "o"):
        word += "es"
    elif word[-1] == "y" and word[-2].lower() not in ("a", "e", "i", "o", "u"):
        word = word[:-1] + "ies"
    elif word[-1] == "f":
        word = word[:-1] + "ves"
    elif word[-2:] == "fe":
        word = word[:-2] + "ves"
    else:
        word += "s"

    return word


for line in sys.stdin:
    s = line.strip()

    print(pluralize(s))
