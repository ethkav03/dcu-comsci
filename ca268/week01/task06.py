#!/usr/bin/env python3

class Employee(object):
    def __init__(self, fullname, **optional):
        self.firstname = fullname.split()[0]
        self.lastname = fullname.split()[1]
        for key, value in optional.items():
            setattr(self, key, f"{value}")


def main():
    tom = Employee('Tom Ford')
    john = Employee('John Travolta', nationality='American')
    jack = Employee('Jack Nicholson', nationality='American', age=84)

    print(jack.age) # 84
    print(tom.firstname) # 'Tom'
    print(john.lastname) # 'Travolta'
    print(john.nationality)


if __name__ == "__main__":
    main()