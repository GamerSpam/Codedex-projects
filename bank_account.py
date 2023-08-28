# Bank Account lesson from Codedex

class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, a):
        self.balance += a
        return self.balance

    def withdraw(self, a):
        self.balance -= a
        return self.balance
    def display_balance(self):
        print(self.balance)

spam = BankAccount('Gamer', 'Spam', 256823, 'Checking', 2865, 8000.63)

spam.deposit(96)
spam.withdraw(25)
spam.display_balance()