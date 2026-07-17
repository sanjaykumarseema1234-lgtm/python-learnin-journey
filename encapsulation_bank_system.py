class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance shouldn't be negative!")
           
    def deposit(self,amount):
    	if amount >= 0:
    		self.__balance += amount
    	else:
    		print("balance should be graeter then zero!")
 
    def get_balance(self):
        return self.__balance
       

a1 = BankAccount("Sanjay", 1000)

a1.set_balance(2000)

a1.deposit(3000)

print(a1.get_balance())
