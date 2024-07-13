class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
# main-0.py

from bank_account import BankAccount
import sys

def main():
    # Create an instance of the BankAccount class
    account = BankAccount()

    # Check if command line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: main-0.py <operation> <amount>")
        return

    operation = sys.argv[1]

    if operation == 'deposit':
        if len(sys.argv) < 3:
            print("Please provide the amount to deposit")
            return
        amount = float(sys.argv[2])
        account.deposit(amount)
        print(f"Deposited {amount} successfully")
    elif operation == 'withdraw':
        if len(sys.argv) < 3:
            print("Please provide the amount to withdraw")
            return
        amount = float(sys.argv[2])
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew {amount} successfully")
        else:
            print("Insufficient funds for withdrawal")
    elif operation == 'balance':
        print(f"Current balance: {account.get_balance()}")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
     