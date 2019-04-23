class M-pesaAccount:
	def __init__(self,name,number,balance):
		self.name = name
		self.number = number
		self.balance = balance

	def withdrawal_amount(self,s):
		withdrawal_amount = s
		s < self.balance
		self.balance = self.balance - s
		message = "Confirmed.You have withdrawn {} Ksh from your account.Your balance is {} Ksh".format(self.name,s,self.balance)
		print(message)

	def deposit (self,q):
		deposit = q
		self.balance = self.balance + q
		message = "Confirmed.You have deposited {} Ksh in your account.Your balance is {} Ksh".format(self.name,q,self.balance)
		print(message)

	def account_balance(self):
		account_balance = self.balance
		message = "Confirmed your M-PESA balance was {} Ksh".format(self.name,self.balance)
		print(message)