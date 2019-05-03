import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

cur.execute("SELECT UnitPrice, Quantity, UnitPrice*Quantity AS TotalPrice, OrderID, ProductID FROM OrderDetails")
print("Price details for orders:")
print("UnitPrice Quantity TotalPrice OrderID ProductID")
for row in cur:
    print(row)

cur.close()
conn.close()