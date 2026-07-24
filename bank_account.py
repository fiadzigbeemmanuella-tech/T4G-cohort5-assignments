class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit failed: Amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"GHS {amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal failed: Amount must be greater than zero.")

        elif amount > 5000:
            print("Withdrawal failed: Maximum daily withdrawal is GHS 5000.")

        elif amount > self.balance:
            print("Withdrawal failed: Insufficient funds.")

        else:
            self.balance -= amount
            print(f"GHS {amount:.2f} withdrawn successfully.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_holder}] | Balance: GHS {self.balance:.2f}"


# Demonstration
if __name__ == "__main__":
    print("Transactions:")

    # Creating two BankAccount instances
    account1 = BankAccount("Yvonne Devor", 1000)
    account2 = BankAccount("Rosebud Sedem", 6000)

    # Successful transactions
    account1.deposit(500)
    account1.withdraw(400)
    account2.withdraw(5000)

    print("\nAccount Details:")
    print(account1)
    print(account2)

    # Failed transactions
    print("\nFailed Transactions:")

    # Withdrawal above daily limit
    account2.withdraw(6000)

    # Withdrawal more than available balance
    account1.withdraw(2000)

    # Negative withdrawal
    account1.withdraw(-200)

    # Zero withdrawal
    account1.withdraw(0)