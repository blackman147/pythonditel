class Credit_limit_calculator:
    account_number = 0
    current_balance = 0
    total_charges = 0
    total_credits = 0
    new_balance = 0

    def calculator(self):

        self.account_number = int(input("Enter your account number: "))
        self.current_balance = int(input("Enter your current balance: "))
        self.total_charges = int(input("Enter the total of all charges this month: "))
        self.total_credits= int(input("Enter total credits requested this month: "))

        self.new_balance = self.current_balance + (self.total_charges - self.total_credits)

        if self.new_balance > self.total_credits:
            print("credit limit exceeded")
        else:
            print("credit limit exceeded")

    def display(self):
        print("your account balance is: " + str(self.account_number))
        print("your current balance is: " + str( self.current_balance))
        print("your total charges for this month is: " + str(self.total_charges))
        print("your total credit fir this month is: " + str(self.total_credits))
        print("your new account balance is: " + str(self.new_balance))


def main():
    clc = Credit_limit_calculator()
    clc.calculator()
    clc.display()


main()
