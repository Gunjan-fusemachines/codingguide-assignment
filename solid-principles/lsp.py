class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds!")

class CheckingAccount:
    def __init__(self, balance, overdraft_limit):
        self.savings_account = BankAccount(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.savings_account.balance + self.overdraft_limit:
            self.savings_account.withdraw(amount)
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account):
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)

if __name__ == "__main__":
    savings_account = BankAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)
