"""
File stock.py
Manages a stock's attributes
"""
class Stock:
    """
    Represents a companies stock and the price of individual shares.
    """
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        """
        @param previousClosingPrice - The stock price from a day ago.
        """
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice
    def getChangePercent(self):
        """
        Returns the percent change of currentPrice -> previousClosingPrice
        """
        return (self.currentPrice/self.previousClosingPrice)*100
    def getName(self):
        """ Returns stock's name """
        return self.name
    def getSymbol(self):
        """ Returns stock's symbol """
        return self.symbol
    def getPreviousClosingPrice(self):
        """ Returns stock's closing price """
        return self.previousClosingPrice
    def getCurrentPrice(self):
        """ Returns stock's current price"""
        return self.currentPrice
    def setPreviousClosingPrice(self, price):
        """ Modifies stock's closing price """
        self.previousClosingPrice = price
    def setCurrentPrice(self, price):
        """ Modifies stock's current price """
        self.currentPrice = price

# googleStock = Stock("GOOGL", "Alphabet Inc Class A", 1116.56, 1116.19)
# googleStock.setCurrentPrice(1420.69)
# print(googleStock.getChangePercent(), "%")