class BankAccount:

	def __init__(self,account_balance):
		self.account_balance = 0

	def deposit(self, amount):
		self.account_balance += amount
		return self.account_balance
		
	def withdraw(self, amount):
        	if 0 < amount <= self.account_balance :
            		self.account_balance -= amount
            		return True  
        	else:
            		return False

	def display_balance(self):
		print(f"Current Balance: ${self.account_balance}")
