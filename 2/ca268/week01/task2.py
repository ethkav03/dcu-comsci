#!/usr/bin/env python3

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is {self.age} years old"

    def get_height(self):
        return f"{self.name} is {self.height} cm tall"

    def get_weight(self):
        return f"{self.name} is {self.weight} kg"


def main():
    p1 = Person("Ethan", "19", "179", "96")
    print(p1.get_age())
    print(p1.get_height())
    print(p1.get_weight())


if __name__ == "__main__":
    main()