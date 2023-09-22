class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive amount."
        else:
            return "Insufficient balance for withdrawal."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"

# Create an instance of the BankAccount class
account1 = BankAccount("123456", "John Doe", 1000.0)

# Test the deposit and withdrawal functionality
print(account1.display_balance())
print(account1.deposit(500.0))
print(account1.withdraw(200.0))
print(account1.display_balance())