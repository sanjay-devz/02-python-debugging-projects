class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def set_amount(self,amount):
        self.amount = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print(f"Customer : {self.name}")
        print(f"Balance  : ₹{self.balance}")
        print("-" * 25)


accounts = [
    BankAccount("Alice", 5000,),
    BankAccount("Bob", 3500),
    BankAccount("Charlie", 7000)
]


def total_balance(data):
    total = 0

    for account in data:
        total += account.balance

    return total


accounts[0].deposit(1500)

accounts[1].withdraw(4000)

accounts[2].withdraw(2000)

print("ACCOUNT SUMMARY\n")

for account in accounts:
    account.display()

print("Total Bank Balance:", total_balance(accounts))

richest = max(accounts, key=lambda accounts: accounts.balance)

print("\nRichest Customer:")
richest.display()

accounts.append(BankAccount("David", 4000))

print("\nUpdated Total Balance:", total_balance(accounts))  