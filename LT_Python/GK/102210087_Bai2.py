class Account:
    def __init__(self, account_number, account_holder, opening_balance, type_of_account):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = opening_balance
        self.type_of_account = type_of_account

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance
    def __str__(self):
        return f"Account[{self.account_number}] - {self.account_holder}, {self.type_of_account} = {self.balance:.2f}"