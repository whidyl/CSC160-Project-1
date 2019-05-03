import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

cur.execute("SELECT SupplierID, ContactName, ContactTitle FROM Suppliers WHERE NOT ContactTitle=?", ('Marketing Manager',))

print("Supplier info for non marketing managers:")
print("SupplierID   ContactName    ContactTitle")
for row in cur:
    print(row)

cur.close()
conn.close()