#!/usr/bin/env python3

class Deque:
    def __init__(self):
        self.items = []

    def add_end(self, n):
        self.items.append(n)

    def remove_end(self, n):
        self.items.pop()

    def add_start(self, n):
        self.items.insert(0, n)

    def remove_start(self):
        self.items.pop(0)

    def first(self):
        return self.items[0]

    def last(self):
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self) == 0

    def __str__(self):
        return f"{self.items}"


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    dq = Deque()
    for num in nums[3:]:
        dq.add_end(num)
    print(dq)
    for num in nums[:3]:
        dq.add_start(num)
    print(dq)
    print(dq.is_empty())


if __name__ == "__main__":
    main()