# Program that creates the class bankAccount and it's methods

# class definition
class BankAccount():
    def __init__(self, accountNum = int, name = str, balance = 0):
        self.accountNum = accountNum
        self.name = name
        self.balance = balance
        print('Bank account successfully created.')

    def changeName(self, newName):
        self.name = newName
        print('Name successfully changed.')

    def deposit(self, value):
        self.balance += value
        print(f'Successfully deposited $ {value}.')

    def withdraw(self, value):
        if self.balance < value:
            print('Insufficient money on your account.')
        else:
            self.balance -= value
            print(f'Successfully withdrawn $ {value}')

    def printBalance(self):
        print(f'Your actual balance is $ {self.balance}')

# main program

# create objects of the class to use it's methods
account1 = BankAccount(1, 'Marcos')
account2 = BankAccount(2, 'Gabriela', 10000)
account3 = BankAccount(3, 'Marcela', 200000)

account1.deposit(5000)
account2.withdraw(8000)
account3.withdraw(300000)

account1.printBalance()
account2.printBalance()
account3.printBalance()
