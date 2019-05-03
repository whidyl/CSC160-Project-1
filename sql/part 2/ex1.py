"""  Write a Python program that shows for each Product, the associated Supplier. 
(See the JOIN clause in SQL). Display ProductID, ProductName, and the CompanyName 
of the Supplier. Sort the result by ProductID. """

import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
SELECT ProductID, ProductName, CompanyName 
  FROM Products JOIN Suppliers
    ON Products.SupplierID = Suppliers.SupplierID 
;
"""

cur.execute(query)
print("Each product and it's associated supplier:")
print("ProductID   ProductName    CompanyName")
for row in cur:
    print(row)

cur.close()
conn.close()