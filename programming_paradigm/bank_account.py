class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: R{amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: R{amount}")
            return True
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            return False

    def display_balance(self):
        print(f"Current Balance: R{self.__account_balance}")
