#!/usr/bin/env python3

import sys

runners = sys.stdin.readlines()

times = {}

for runner in runners:
   a = runner.strip().split()
   times[a[0]] = a[1:]

fastest_runner = ""
fastest_time = 9999999999

for k, v in times.items():
   for pair in v:
      try:
         time = (int(pair[:-3]) * 60) + int(pair[-2:])
      except ValueError:
         break
      if time < fastest_time:
         fastest_runner = k
         fastest_time = time

start = fastest_time // 60
end = fastest_time % 60

print(f'{fastest_runner} : {start}:{end}')
