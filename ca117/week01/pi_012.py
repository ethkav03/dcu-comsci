#!/usr/bin/env python3

import sys
from math import pi

for n in sys.stdin:
    print(f"{pi:.{int(n)}f}")
