#!/usr/bin/env python3

with open("input.txt") as f:
   text = f.read()

print(text[:len(text) - 1])
