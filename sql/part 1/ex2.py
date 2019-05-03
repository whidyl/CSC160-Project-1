import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

cur.execute("SELECT * FROM Employees")

print("Names and hire data for sales reps:")
for row in cur:
    if (row[3] == "Sales Representative"):
        print(row[1] + ", " + row[2] + ": " + row[6])

cur.close()
conn.close()