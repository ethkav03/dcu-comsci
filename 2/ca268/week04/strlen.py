#!/usr/bin/env python3

def main():
    print(string_length("Hello, world!"))

def string_length(s):
    if s == "":
        return 0;
    return 1 + string_length(s[1:])


if __name__ == "__main__":
    main()