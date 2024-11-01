class BankAccount(object):
    def set_attributes(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def print_attributes(self):
        print("Name:", self.name)
        print("Account number:", self.number)
        print(f"Balance: {self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
