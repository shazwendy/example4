class MpesaAccount:
	def __init__(self,name,phone_number,balance):
		self.name = name
		self.phone_number = phone_number
		self.balance = 0
		self.deposits = []
		self.withdrawals = []
		self.loan = 0

	def deposit(self,amount):
		self.balance = self.balance + amount
		self.deposits.append(amount)
		message1 = "Confirmed {} You have deposited {} Ksh in your account.Your new balance is {} Ksh".format(self.name,amount,self.balance)
		print(message1)

	def withdrawal(self,amount):
		if amount<self.balance:
		    self.balance = self.balance - amount
			self.withdrawas.append(amount) 
			message5 = "Confirmed {} You have withdrawn {} Ksh from your account.Your balance is {} Ksh".format(self.name,s,self.balance)
			print (message5)
        else:
        	print("insuffucient balance")

     def account_balance(self):
		account_balance = self.balance
		message4 = "Confirmed {} Your balance was {} Ksh".format(self.name,self.balance)
		print(message4)   	

	
	def my_deposits(self):
		for d in self.deposits:
			print(d)

	def my_withdrawals(self):
		for j in self.withdrawals:
			print(j)

	def give loans(self,amount):
		if len(self.deposits)>=5 and amount<1/3*sum(self.deposits) and self.loan==0:
			self.loan=self.loan + amount
			print ("Hello {}, you have gotten {}".format(self.name, amount))
		else:
			print("Hello {}, you are not qualified for this loan".format(self.name))

	def pay loan(self,amount):
		if self.loan==0:
			print("you do not have a loan debt")
		elif amount<self.loan:
			self.loan=self.loan-amount
			print("Hi {} you have paid {} as part of your loan repayment. Your remaining balance is {}".format(self.name, amount, self.loan))
		elif amount==self.loan:
			self.loan=self.loan-amount
			print("You have completed the payment of your loan")
		elif amount>self.loan
			more=amount-self.loan
			self.balance=more+self.balance
			self.loan=amount-self.loan-more
			print("Hello {} you have paid more than what is needed, your new balance is {}".format(self.name,self.balance))




		
	