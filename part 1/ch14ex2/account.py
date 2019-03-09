"""
File account.py
Manages Account object
"""

class Account():
    """ Represents an account used to manage money """
    def __init__(self, id=0, balance=100.0, annualInterestRate=0.0):
        """ 
        Constructs an account with a default balance of 100
        @param annualInterestRate - represented as a percentage. 1 = 1%
        """
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate
    def getAnnualInterestRate(self):
        """ Returns account's annualInterestRate """
        return self.annualInterestRate
    def getBalance(self):
        """ Returns account's balance """
        return self.balance
    def getId(self):
        """ Returns account's id """
        return self.id
    def setAnnualInterestRate(self, rate):
        """ Sets account's annualInterestRate """
        self.annualInterestRate = rate
    def setBalance(self, balance):
        """ Sets account's balance """
        self.balance = balance
    def setId(self, id):
        """ Sets account's id """
        self.id = id
    def getMonthlyInterestRate(self):
        """ Returns monthly interest rate """
        return self.getAnnualInterestRate()/12
    def getMonthlyInterest(self):
        """ Returns interest accumulated in a months time """
                                # \/ divide by 100 to convert from percentage
        return self.getBalance()*(self.getMonthlyInterestRate()/100)
    def withdraw(self, amount):
        """ Removes money from account """
        self.setBalance(self.getBalance() - amount)
    def deposit(self, amount):
        """ Adds money to account """
        self.setBalance(self.getBalance() + amount)
