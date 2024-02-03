class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep):
        self.balance += dep
        print('Deposit accepted!')

    def withdraw(self, wd):
        if self.balance >= wd:
            self.balance -= wd
            print('Withdrawal accepted!')
        else:
            print('Insufficient balance!')