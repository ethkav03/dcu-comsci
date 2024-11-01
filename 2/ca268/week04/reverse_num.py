#!/usr/bin/env python3

def main():
    print(reverse_num(123))

def reverse_num(n):
    n = str(n)
    if len(n) == 0:
        return ''
    return n[-1] + reverse_num(n[:-1])


if __name__ == "__main__":
    main()