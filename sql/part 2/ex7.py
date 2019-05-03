"""  Write a Python program that displays a list of all customers sorted 
alphabetically by region. Customers with no region (the region field an empty 
string) should not be listed. Sort by region, and within each region sort by 
CustomerID """

import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
  SELECT Region, CustomerID
    FROM Customers
   WHERE Region != ""
ORDER BY Region ASC, CustomerID ASC
;
"""

cur.execute(query)
print("All customers with an associated region sorted alphabetically.")
print("Region  CustomerID")
for row in cur:
    print(row)

cur.close()
conn.close()