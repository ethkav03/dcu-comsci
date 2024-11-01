#!/usr/bin/env python3

import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return f"{self.items}"


def main():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    s = Stack()
    for num in nums:
        s.push(num)

    for num in nums:
        top = s.peek()
        print(top)
        popped = s.pop()
        print(s)
        


if __name__ == "__main__":
    main()