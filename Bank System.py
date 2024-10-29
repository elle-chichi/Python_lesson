class Account:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive and not exceed the balance.")

    def check_balance(self):
        return f"Account balance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, account_holder, account_number, initial_balance=0, interest_rate=0.01):
        super().__init__(account_holder, account_number, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: {interest}. New balance: {self.balance}")

class CheckingAccount(Account):
    def __init__(self, account_holder, account_number, initial_balance=0, overdraft_limit=0):
        super().__init__(account_holder, account_number, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount exceeds the available balance and overdraft limit.")

# Example usage
if __name__ == "__main__":
    savings = SavingsAccount("Alice", "S123", 1000)
    checking = CheckingAccount("Bob", "C456", 500, overdraft_limit=200)

    savings.deposit(200)
    savings.withdraw(100)
    savings.add_interest()
    print(savings.check_balance())

    checking.withdraw(600)
    print(checking.check_balance())
