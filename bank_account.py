class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        return self
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds charging a $5 fee")
            self.balance -= 5
        return self    
        
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
    
    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            account.display_account_info()


harini = BankAccount(0.01,0)
pk = BankAccount(0.02,0)

harini.deposit(200).deposit(300).deposit(400).withdraw(300).yield_interest().display_account_info()
pk.deposit(200).deposit(1300).withdraw(50).withdraw(10).withdraw(300).withdraw(100).yield_interest().display_account_info()
print("=" * 80)
BankAccount.all_instances()