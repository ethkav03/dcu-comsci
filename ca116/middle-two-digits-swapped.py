#!/usr/bin/env python3

n = int(input())

first_three_digits = n // 1000
first_two_digits = n // 10000

start = n // 10000
end = n // 100

not_swapped = end - (start * 100)

digit_one = not_swapped // 10
digit_two = not_swapped - (digit_one * 10)

final = digit_one + (digit_two * 10)
print(final)
