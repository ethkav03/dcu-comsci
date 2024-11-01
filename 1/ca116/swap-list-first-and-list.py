#!/usr/bin/env python3

import sys

a = sys.argv[1:]

tmp = a[0]
a[0] = a[len(a) - 1]
a[len(a) - 1] = tmp
