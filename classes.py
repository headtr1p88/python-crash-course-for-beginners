class Account:
    bank = 'World bank'
    def __init__(self, type, balance):
        self.type = type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Your new balance is {self.balance}')

    def withdraw(self, amount):
        temp_balance = self.balance - amount

        if temp_balance < 0:
            print(f'Insufficient funds. Your balance is {self.balance}')
        else:
            self.balance -= amount
            print(f'Your new balance is {self.balance}')

my_account = Account('Savings', 10000)
my_account.withdraw(11000)