from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)

    def __str__(self):
        return f"SavingsAccount[{self.account_holder}] | Balance: GHS {self.balance:.2f} | Rate: {self.interest_rate}%"


# Demonstration

print("Savings Account Transactions:")

# Creating a SavingsAccount
savings = SavingsAccount("Yvonne Devor", 500, 5)

# Making two deposits
savings.deposit(200)
savings.deposit(300)

print("\nBefore Interest:")
print(savings)

# Applying interest
print("\nApplying Interest:")
savings.apply_interest()

print("\nAfter Interest:")
print(savings)

# Making a withdrawal
print("\nWithdrawal:")
savings.withdraw(400)

print("\nFinal Account Details:")
print(savings)