#!/usr/bin/env python3

from operator import truediv


def main():
    print(is_heteromecic(110))
    print(is_heteromecic(4))
    print(is_heteromecic(6))
    print(is_heteromecic(12))

def is_heteromecic(num, n=1):
    if n > num // 2 + 1:
        return False
    elif n * (n + 1) == num:
        return True
    else:
        return is_heteromecic(num, n + 1)
    


if __name__ == "__main__":
    main()