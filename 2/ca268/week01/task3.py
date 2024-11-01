#!/usr/bin/env python3

class Class4:
    def __init__(self, fname, lname, age):
        self.d = {
            'fname':fname,
            'lname':lname,
            'age':age,
        }


def sort_class4(classes, key):
    return sorted(classes, key=lambda x: x.d[key]);


def main():
    p1 = Class4('Barack', 'Obama', 40)
    p2 = Class4('Abraham', 'Lincoln', 21)
    p3 = Class4('Donald', 'Trump', 14)

    print([p1, p2, p3])
    print(sort_class4([p1, p2, p3], 'fname'))
    print(sort_class4([p1, p2, p3], 'lname'))
    print(sort_class4([p1, p2, p3], 'age'))


if __name__ == "__main__":
    main()