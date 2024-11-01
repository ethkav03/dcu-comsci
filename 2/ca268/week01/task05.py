#!/usr/bin/env python3

class Pizza():
    counter = 0
    def __init__(self, ingredients):
        Pizza.counter += 1
        self.order_number = Pizza.__counter
        self.ingredients = ingredients

    def diavola():
        return Pizza(['Mozzarella', 'Spicy sausage', 'Pomodorino tomatoes'])

    def serrano():
        return Pizza(['Black olives', 'Red onion', 'Cooked picadillo'])
    
    def margherita():
        return Pizza(['Red tomatoes', 'White mozzarella', 'Green basil'])


def main():
    p1 = Pizza(['Black olives', 'Red onion', 'Meatballs'])
    p2 = Pizza.diavola()

    print(p1.order_number) # 1
    print(p2.ingredients) # ['Mozzarella', 'Spicy sausage', 'Pomodorino tomatoes']
    print(p1.ingredients)
    print(p2.order_number)


if __name__ == "__main__":
    main()