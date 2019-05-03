""" Write a Python program that displays the three highest values for average 
overall freight for ship countries in descending order by average freight. 
(Use the Freight and ShipCountry fields in the Orders table. """

import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
  SELECT Freight, ShipCountry
    FROM Orders
ORDER BY Freight DESC
   LIMIT 3
;
"""

cur.execute(query)
print("All customers with an associated region sorted alphabetically.")
print("Region  CustomerID")
for row in cur:
    print(row)

cur.close()
conn.close()