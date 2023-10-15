class Account:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money > self.balance:
            print("Error: low balance")
        else:
            self.balance -= money
            print("Success")

a = Account("Zhaniya", 0)
a.deposit(10)
a.withdraw(10)