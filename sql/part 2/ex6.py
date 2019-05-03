""" Write a Python program that displays the Products in inventory that should
be reordered. Display the ProductID, ProductName, UnitsInStock, 
and ReorderLevel. This time, define “products that need reordering” as:
• UnitsInStock plus UnitsOnOrder is less than or equal to the ReorderLevel
• The Discontinued flag is false (0) """

import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
  SELECT ProductID, ProductName, UnitsInStock, ReorderLevel
    FROM Products
   WHERE (UnitsInStock + Products.UnitsOnOrder) <= ReorderLevel 
        AND NOT Products.Discontinued
;
"""

cur.execute(query)
print("Products in inventory that should be reordered.")
print("ProductID  ProductName  UnitsInStock  ReoderLevel")
for row in cur:
    print(row)

cur.close()
conn.close()