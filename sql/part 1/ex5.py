import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

cur.execute("SELECT OrderID, OrderDate FROM Orders WHERE EmployeeID=5")

print("Order info for Steven Buchman")
print("OrderID   OrderDate")
for row in cur:
    print(row)

cur.close()
conn.close()