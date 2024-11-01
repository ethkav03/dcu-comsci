#Name: Ethan Kavanagh
#Student ID: 2134487

#01. get_email.py
class Person:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def get_email(self):
        return "{}.{}@dcu.ie".format(self.fname, self.lname)

#02. task02.py
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

#03. task03.py
class Class4:
    def __init__(self, fname, lname, age):
        self.d = {
            'fname':fname,
            'lname':lname,
            'age':age,
        }


def sort_class4(classes, key):
    return sorted(classes, key=lambda x: x.d[key]);

#04. task04.py
class Smoothie:
    def __init__(self, ingredient):
        self.ingredient = ingredient

    def get_cost(self):
        prices = {
            'Banana':0.50,
            'Strawberries':1.50,
            'Mango':2.50,
            'Blueberries':1.00,
            'Raspberries':1.00,
            'Apple':1.75,
            'Pineapple':3.50,
        }
        total = 0
        for s in self.ingredient:
            if s in self.ingredient:
                total += prices[s]
        return "€{:.2f}".format(total)

    def get_price(self):
        return "€{:.2f}".format(float(self.get_cost().lstrip("€")) + 2.5)

    def get_name(self):
        return "{} Fusion".format(" ".join(self.ingredient))

#05. task05.py
class Pizza():
    __counter = 0
    def __init__(self, ingredients):
        Pizza.__counter += 1
        self.order_number = Pizza.__counter
        self.ingredients = ingredients

    def diavola():
        return Pizza(['Mozzarella', 'Spicy sausage', 'Pomodorino tomatoes'])

    def serrano():
        return Pizza(['Black olives', 'Red onion', 'Cooked picadillo'])
    
    def margherita():
        return Pizza(['Red tomatoes', 'White mozzarella', 'Green basil'])

#06. task06.py
class Employee(object):
    def __init__(self, fullname, **optional):
        self.firstname = fullname.split()[0]
        self.lastname = fullname.split()[1]
        for key, value in optional.items():
            setattr(self, key, f"{value}")