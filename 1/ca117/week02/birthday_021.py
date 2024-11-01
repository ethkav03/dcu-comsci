#!usr/bin/env python3

import calendar
import sys

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
poemlines = ["Monday's child is fair of face.", "Tuesday's child is full of grace.", "Wednesday's child is full of woe.", "Thursday's child has far to go.", "Friday's child is loving and giving.", "Saturday's child works hard for a living.", "Sunday's child is fair and wise and good in every way."]

for line in sys.stdin:
    [day, month, year] = line.strip().split()
    weekday = calendar.weekday(int(year), int(month), int(day))
    print(f'You were born on a {weekdays[weekday]} and {poemlines[weekday]}')
