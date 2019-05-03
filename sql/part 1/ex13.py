import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

query = """
--sql
SELECT ContactTitle, COUNT(ContactTitle) AS ContactCount
FROM Customers 
GROUP BY ContactTitle
ORDER BY ContactCount DESC
;
"""

cur.execute(query)
print("Title count for each title:")
for row in cur:
    print(row)

cur.close()
conn.close()