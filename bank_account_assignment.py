class BankAccount:

    def __init__(self, account_number: str, balance : float, owner: str, type: str):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type

    def __repr__(self):
        return f"Account Number: {self.account_number} \nBalance: {self.balance} \nAccount Owner: {self.owner} \n Account Type : {self.type} "

class Bank:
    def __init__(self, name : str , accounts: list ["BankAccount"]): 
        self.name = name
        self.accounts = accounts
   
    def __repr__(self):
        return f"Bank Name: {self.name}"

    def add_account(self, account):
        self.accounts.append(account)


class Customer:

    def __init__(self, name : str , accounts : list [BankAccount]):
        self.name = name
        self.accounts = accounts
    
    def __repr__(self):
        return f"Customer Name : {self.name}"

    def add_account(self, account):
        self.accounts.append(account)

class Transactions:
    def __init__(self, account:"BankAccount", amount : float, type : str):
        self.account = account
        self.amount = amount
        self.type = type

    def activities (self):
        if self.type == "Credit":
            self.account.balance = self.account.balance + self.amount
        if self.type == "Debit" and self.account.balance >= self.amount:
            self.account = self.account.balance - self.amount




# Create a new bank object
bank = Bank ("My Bank", [])
print( "Bank object has been created")

# Create a new customer object
customer = Customer("Musinguzi Rodney", [])

# Create a new BankAccount object
bankAccount = BankAccount (102010355, 1000000, "Musinguzi Rodney", "Savings")

# Add the BankAccount object to the Bank object
bank.add_account(bankAccount)



# Add the BankAccount object to the Customer object
customer.add_account(bankAccount)


# Print the Bank object
print(bank)

# Print the Customer object
print (customer)

# Print the BankAccount object
print (bankAccount)

# Create a new Transaction object

action = Transactions(bankAccount, 200000, "fixed deposit")
# Add the Transaction object to the BankAccount object


