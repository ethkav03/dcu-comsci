#!/usr/bin/env python3

from random import randint

class HashTable:
    def __init__(self, size):
        self.slots = [[]] * size
        self.a = randint(1, size)
        self.b = randint(0, size)
        self.p = self.next_prime(size + 1)

    def push(self, name, size):
        index = self.get_index(name, size)
        self.slots[index].append(name)

    def get_index(self, string, size):
        if size == 1:
            return 0;
        return ((self.a * hash(string) + self.b) % self.p) % size

    def next_prime(self, p):
        while not self.is_prime(p):
            p += 1
        return p
        
    def is_prime(self, n, i=2):
        if n == i:
            return True
        elif n % i == 0:
            return False
        return self.is_prime(n, i+1)
    
    def __str__(self):
        return f"{self.slots}"


def main():
    names = ["Ava", "Brian", "Clóda", "David", "Ethan", "Fionn", "Gary"]

    h = HashTable(len(names))
    for name in names:
        h.push(name, len(names))
    print(h)


if __name__ == "__main__":
    main()