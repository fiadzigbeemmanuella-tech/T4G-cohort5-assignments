class BankAccount:

    # Initialization
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Add money to the account
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit failed: Amount must be greater than GHS 0.")
        else:
            self.balance += amount
            print(f"GHS {amount:.2f} deposited successfully.")

    # Remove money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal failed: Amount must be greater than GHS 0.")

        elif amount > 5000:
            print("Withdrawal failed: Maximum daily withdrawal is GHS 5000.")

        elif self.balance - amount < 50:
            print("Withdrawal failed: You must maintain a minimum balance of GHS 50.")

        else:
            self.balance -= amount
            print(f"GHS {amount:.2f} withdrawn successfully.")

    # Return the current balance
    def get_balance(self):
        return self.balance

    # Display account information
    def __str__(self):
        return f"Account[{self.name}] | Balance: GHS {self.balance:.2f}"

# Demonstration

# Create two bank accounts
account1 = BankAccount("Yvonne Devor", 1000)
account2 = BankAccount("Rosebud Sedem", 6000)

# Make transactions
account1.deposit(500)       # Balance = 1500
account1.withdraw(400)      # Balance = 1100
account2.withdraw(5000)     # Balance = 1000

# Print accounts after transactions
print("\nAccount Details:")
print(account1)
print(account2)

# Attempting a withdrawal that should fail
print("\nFailed Transaction:")
account2.withdraw(5500)