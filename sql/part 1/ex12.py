import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
SELECT DISTINCT Country 
FROM Customers 
ORDER BY Country DESC
;
"""

cur.execute(query)
print("Total number of customers:")
for row in cur:
    print(row)

cur.close()
conn.close()