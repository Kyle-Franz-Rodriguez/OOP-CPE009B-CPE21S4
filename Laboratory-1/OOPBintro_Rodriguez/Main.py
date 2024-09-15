"""Main"""

import Accounts
import ATM

#Create Account
Account1 = Accounts.Accounts(123456,"Royce","Chua",1000,"Silver Street Quezon City","roycechua123@gmail.com")

print("Account 1")
print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)
print("")

Account2 = Accounts.Accounts(654321,"John","Doe",2000,"Gold Street Quezon City","johndoe@yahoo.com")

print("Account2")
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)
print("")

#Create ATM
print("-ATM-")
print("Account1")
ATM1 = ATM.ATM(123456)
ATM1.deposit(Account1, 500)
ATM1.check_balance(Account1)
ATM1.view_transactionsummary(500, 0)
print("")
ATM2 = ATM.ATM(654321)
ATM2.deposit(Account2, 300)
ATM2.check_balance(Account2)
ATM2.view_transactionsummary(300, 0)