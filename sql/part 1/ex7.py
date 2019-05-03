import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

cur.execute("SELECT ProductID, ProductName FROM Products WHERE ProductName LIKE '%queso%'")

print("Info for queso products:")
print("ProductID  ProductName")
for row in cur:
    print(row)

cur.close()
conn.close()