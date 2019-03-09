from account import Account


myAccount = Account(1122, 20000, 4.5)
myAccount.withdraw(2500)
myAccount.deposit(3000)
myOtherAccount = Account(1133, 10900, 4)
print(myAccount.balance)
print(myOtherAccount.balance)
"""
print("ID:", myAccount.getId())
print("Balance:", myAccount.getBalance())
print("Monthly Interest Rate:", myAccount.getMonthlyInterestRate())
print("Monthly Interest:", myAccount.getMonthlyInterest())
"""
