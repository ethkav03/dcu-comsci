#!/usr/bin/env python3

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, n):
        self.items.append(n)

    def first(self):
        return self.items[0]

    def dequeue(self):
        self.items.pop(0)

    def __str__(self):
        return f"{self.items}"


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    q = Queue()
    for num in nums:
        q.enqueue(num)

    for num in nums:
        print(q.first())
        q.dequeue()
        print(q)


if __name__ == "__main__":
    main()