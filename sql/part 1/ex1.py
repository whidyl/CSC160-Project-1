import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

cur.execute("SELECT * FROM Categories")

print("All records for CategoryName and Description:")
for row in cur:
    print(row[1] + ": " + row[2])

cur.close()
conn.close()