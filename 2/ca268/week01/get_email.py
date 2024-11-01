#!/usr/bin/env python3

class Person:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def get_email(self):
        return "{}.{}@dcu.ie".format(self.fname, self.lname)