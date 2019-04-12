""" This module provides functionality for importing and analyzing stock data. """
import math
import matplotlib.pyplot as plt
import csv

class StockHistory():
    """ Encapsulates history of stock data for specified csv file """
    def __init__(self, file):
        self.data = {"date": [], "open":[], "high":[], "low":[], "close":[], "adjclose":[], "volume":[]}

        with open(file) as csvFile:
            csvReader = csv.reader(csvFile, delimiter = ',')
            firstRow = True
            for row in csvReader:
                if firstRow: 
                    firstRow = False
                    continue
                self.data["date"].append(row[0])
                self.data["open"].append(float(row[1]))
                self.data["high"].append(float(row[2]))
                self.data["low"].append(float(row[3]))
                self.data["close"].append(float(row[4]))
                self.data["adjclose"].append(float(row[5]))
                self.data["volume"].append(float(row[6]))
    
    def getPriceCorrelation(self, otherStock):
        """ Compares the closing prices of this stock to another and returns their correlation """
        return correlation(self.data["close"], otherStock.data["close"])
    
    def graph(self, beginningDate, endingDate, title):
        """ Graphs the closing prices over specified range of dates. """
        beginningDateIndex = self.data["date"].index(beginningDate)
        endingDateIndex = self.data["date"].index(endingDate)
        plt.plot(self.data["close"][beginningDateIndex:endingDateIndex])
        plt.title(title)
        plt.xlabel("month (since " + beginningDate + ")")
        plt.ylabel("closing price ($)")
        plt.show()

def mean(l):
    """ Returns the average value of a list of numbers """
    total = 0.0
    for num in l:
        total += num
    return total/len(l)


def standardDev(l):
    """ Returns a measurement for how a list of numbers is spread out from the average """
    meanValue = mean(l)
    total = 0.0
    for num in l:
        total += (num - meanValue)**2
    return math.sqrt(total / (len(l) - 1))

def correlation(xlist, ylist):
    """ Measures the stringth and direction of the relationship between two variables. """
    xbar = mean(xlist)
    ybar = mean(ylist)
    xstd = standardDev(xlist)
    ystd = standardDev(ylist)
    num = 0.0
    for i in range(len(xlist)):
        num = num + (xlist[i]-xbar) * (ylist[i] - ybar)
    corr = num / ((len(xlist)-1) * xstd * ystd)
    return corr

def main():
    appleHistory = StockHistory("AAPL.csv")
    teslaHistory = StockHistory("TSLA.csv")
    appleHistory.graph("2019-01-28", "2019-04-04", "APPL Stock History")
    teslaHistory.graph("2018-10-12", "2019-04-11", "TSLA Stock History")
    print("Correlaton of APPL and TSLA: " + str(appleHistory.getPriceCorrelation(teslaHistory)))

if __name__ == "__main__":
    main()