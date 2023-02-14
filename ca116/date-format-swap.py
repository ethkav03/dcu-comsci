#!/usr/bin/env python3

n = int(input())

first_digits = n // 10000
middle_digits = (n // 100) - (first_digits * 100)
end_digits = n - ((first_digits * 10000) + (middle_digits * 100))

date = end_digits + (first_digits * 100) + (middle_digits * 10000)

print(date)
