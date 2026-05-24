class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        return self.balance


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
        return self.balance
