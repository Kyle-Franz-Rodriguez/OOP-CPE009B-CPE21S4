"""ATM"""

class ATM():
    def __init__(self,serial_number):
        self.serial_number = serial_number
    
    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        print("Deposit Complete")
        
    def widthdraw(self, account, amount):
        account.current_balance = account.current_balance - amount
        print("Withdraw Complete")
    
    def check_balance(self, account):
        print("Current balance:",account.current_balance)
        
    def view_transactionsummary(self, deposit, widthdraw):
        print("---Transaction summary---")
        print("Serial Number:",self.serial_number)
        print("Amount deposited:", deposit)
        print("Amount widthdrawn:",widthdraw)