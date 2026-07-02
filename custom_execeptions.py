class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")

class BankError(Exception):
    pass

class InsufficientFundsError(BankError):
    pass
