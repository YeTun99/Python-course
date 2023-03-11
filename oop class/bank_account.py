class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number= account_number
        self.balance= balance
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount},new balance {self.balance}")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"Withdraw {amount},new balance{self.balance}")
        else:
            print("Insufficient balance")

account1=BankAccount("001",10000)
print("Account number",account1.account_number)
print("Initial balance",account1.balance)

account1.deposit(5000)
account1.withdraw(2000)
account1.withdraw(20000) 