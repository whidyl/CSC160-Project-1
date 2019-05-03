import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

cur.execute("SELECT FirstName, LastName, BirthDate FROM Employees ORDER BY BirthDate ASC")

print("Info about employees:")
print("FirstName  LastName  BirthDate")
for row in cur:
    print(row)

cur.close()
conn.close()