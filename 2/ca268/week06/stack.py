#!/usr/bin/env python3

class Stack:
    '''Python implementation the stack'''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def reverse(self):
        a = []
        for c in self.items[::-1]:
            a.append(c)
        return a


def main():
    n = input()
    s = Stack()
    for c in n:
        s.push(c)

    print(s.items)
    print(s.reverse())


if __name__ == "__main__":
    main()