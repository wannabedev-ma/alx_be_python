class BankAccount:

	def __init__(self,account_balance):
		self.account_balance = 0

	def deposit(amount):
		return account_balance += amount
		
	def withdraw(self, amount):
        	if self.account_balance >= amount:
            		self.account_balance -= amount
            		return True  
        	else:
            		return False

	def display_balance(self):
		print(f"Current Balance: ${self.account_balance}")
