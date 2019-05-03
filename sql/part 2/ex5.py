"""  Write a Python program that displays the Products in inventory 
that should be reordered. Display the ProductID, ProductName, UnitsInStock, 
and ReorderLevel. For now, ignore the fields UnitsOnOrder and Discontinued. 
Sort the results by ProductID """
import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
  SELECT ProductID, ProductName, UnitsInStock, ReorderLevel
    FROM Products
   WHERE UnitsInStock <= ReorderLevel
;
"""

cur.execute(query)
print("Products in inventory that should be reordered.")
print("ProductID  ProductName  UnitsInStock  ReoderLevel")
for row in cur:
    print(row)

cur.close()
conn.close()