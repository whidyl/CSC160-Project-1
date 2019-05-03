import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
SELECT COUNT(*) FROM  
;
"""

cur.execute("SELECT COUNT(*) FROM Customers")
print("Total number of customers:")
for row in cur:
    print(row[0])

cur.close()
conn.close()