"""  Write a Python program that displays the total number of products in 
each category. Sort the results by the total number of products, in descending 
order. (Start by creating a query that shows the CategoryName and all associated 
ProductIDs. Then add a Group By.) """

import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
  SELECT CategoryName, COUNT(ProductID) AS ProductCount
    FROM Products JOIN Categories
      ON Products.CategoryID = Categories.CategoryID
GROUP BY CategoryName
ORDER BY ProductCount DESC
;
"""

cur.execute(query)
print("Number of products in each category:")
print("CategoryName  ProductCount")
for row in cur:
    print(row)

cur.close()
conn.close()