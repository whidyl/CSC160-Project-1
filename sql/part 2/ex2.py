"""  Write a Python program that displays a list of the Orders 
that were shipped by the Shipper: Federal Shipping. Display the 
OrderID and OrderDate. View the Orders and Shippers tables in DB Browser 
for SQLite to see the fields to join on in the tab"""

import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
SELECT OrderID, OrderDate
  FROM Orders JOIN Shippers
    ON Orders.ShipVia = Shippers.ShipperID
 WHERE Shippers.CompanyName = "Federal Shipping" 
;
"""

cur.execute(query)
print("All orders shipped by Federal Shipping:")
print("Order ID, OrderDate")
for row in cur:
    print(row)

cur.close()
conn.close()