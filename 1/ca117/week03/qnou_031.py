#!/usr/bin/env python3

import sys

def qnou(s):
   s = s.strip().lower()
   s = s.replace('qu', '~~')
   return 'q' in s


a = sys.stdin.readlines()
print(f'Words with q but no u: {[s.strip() for s in a if qnou(s)]}')
