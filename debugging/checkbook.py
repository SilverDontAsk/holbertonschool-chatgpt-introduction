#!/usr/bin/python3
import sys
class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance.

    Attributes:
    - balance: A float representing the current balance in the checkbook.
    """

    def __init__(self):
        """
        Initializes a Checkbook object with a balance of 0.0.
        """
        self.balance = 0.0
    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook.

        Parameters:
        - amount: A float representing the amount to be deposited.

        Returns:
        - None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))
        return
    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook, if sufficient funds are available.

        Parameters:
        - amount: A float representing the amount to be withdrawn.

        Returns:
        - None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        return
    def get_balance(self):
        """
        Prints the current balance in the checkbook.

        Returns:
        - None
        """
        print("Current Balance: ${:.2f}".format(self.balance))
        return

def main():
    """
    Main function to interact with the Checkbook class.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
                continue
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
                continue
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
