import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

cur.execute("SELECT OrderID, CustomerID, ShipCountry FROM Orders WHERE ShipCountry=? OR ShipCountry=?", ("France", "Belgium"))

print("Info orders from France or Belgium:")
print("OrderID  CustomerID   ShipCountry")
for row in cur:
    print(row)

cur.close()
conn.close()