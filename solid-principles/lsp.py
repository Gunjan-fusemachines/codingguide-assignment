# Liskov Substitution Principle

# Define a common base class for all accounts
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


# Create a SavingsAccount class that inherits from Account
class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    # Any additional methods or behavior specific to SavingsAccount can be added here


# Create a CheckingAccount class that also inherits from Account
class CheckingAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        else:
            return False

    # Any additional methods or behavior specific to CheckingAccount can be added here


# Example usage of the classes
savings_account = SavingsAccount(1000)
checking_account = CheckingAccount(500, 200)

savings_account.deposit(100)
checking_account.deposit(50)

savings_account.withdraw(200)
checking_account.withdraw(300)

print("Savings Account Balance:", savings_account.get_balance()) 
print("Checking Account Balance:", checking_account.get_balance())
