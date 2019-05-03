"""  Write a Python program that displays the total number of customers 
in the Customers table per Country and City. (You can have multiple fields 
in a Group By clause) """
import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
  SELECT Country, City, COUNT(CustomerID) AS CustomerCount
    FROM Customers
GROUP BY Country, City
;
"""

cur.execute(query)
print("Number of customers in each country/city:")
print("Country   City   CustomerCount")
for row in cur:
    print(row)

cur.close()
conn.close()