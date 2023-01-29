#!/usr/bin/env python3

def main():
    print(reverse_string("hello"))

def reverse_string(s):
    if len(s) == 0:
        return ''
    return s[-1] + reverse_string(s[:-1])


if __name__ == "__main__":
    main()