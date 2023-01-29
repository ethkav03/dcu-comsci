#!/usr/bin/env python3

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


def main():
    drink = Smoothie(['Banana', 'Mango'])
    print(drink.get_cost()) #€3.00
    print(drink.get_price()) #€5.50
    print(drink.get_name()) #Banana Mango Fusion


if __name__ == "__main__":
    main()