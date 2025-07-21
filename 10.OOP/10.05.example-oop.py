# ** Define a class named BankAccount.
# ** Each created object should have an attribute named accountHolder. Example: BankAccount("Sadık Turan")
# ** Each created object should have an attribute named balance, initialized to 0.0.
# ** Define a method named deposit that takes an amount from the user, adds it to the balance, and returns the updated balance.
# ** Define a method named withdraw that takes an amount from the user, subtracts it from the balance, and returns the updated balance.


# account = BankAccount("Sadık Turan")
# account.accountHolder  =>  Sadık Turan
# account.balance        =>  0.0
# account.deposit(1000)  =>  1000.0
# account.withdraw(500)  =>  500.0

class BankAccount:

    def __init__(self,accountHolder):
        self.accountHolder = accountHolder
        self.balance = 0
        
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withDraw(self,amount):
        if(self.balance>= amount):
            self.balance -= amount
            return self.balance
        else:
            print("There is no enough money.")

    def getBalance(self):
        print(f"Your Balance: {self.balance}")


account = BankAccount("Halil İbrahim Kaya")

print(f"Account Holder: {account.accountHolder}")

account.getBalance()

account.deposit(1000)

account.getBalance()

account.withDraw(360)

account.getBalance()

account.withDraw(270)

account.getBalance()
"""
Output:
Account Holder: Halil İbrahim Kaya
Your Balance: 0
Your Balance: 1000
Your Balance: 640
Your Balance: 370
"""