#!/usr/bin/env python3

def main():
    print(reverse_list([1, 2, 3, 4, 5]))

def reverse_list(a):
    if len(a) == 0:
        return []
    return [a.pop()] + reverse_list(a)


if __name__ == "__main__":
    main()