class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello welcome to Blackie bank")

    def deposit(self):
        amount = float(input("Enter Amount to be deposited: "))
        self.balance += amount
        print('/n your account balance is: ', amount)

    def withdraw(self):
        amount = float(input("Enter amount you want to withdraw: "))
        self.balance -= amount
        if amount <= self.balance:
            self.balance -= amount
            print(" your account balance is: ", amount)
        else:
            print("insufficient funds!!! ")

    def display(self):
        print(" net available balance =", self.balance)


s = Bank_Account()

s.deposit()
s.withdraw()
s.display()
