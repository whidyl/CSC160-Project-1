import sqlite3

conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

title = input("Which employees do you want to see? (Sales Representative, Sales Manager, Vice President, Inside Sales Coordinator):")


cur.execute("SELECT FirstName, LastName, HireDate FROM Employees WHERE Title=?", (title,))

print("Names and hire data for " + title + ":")
print("FirstName   LastName   HireDate")
for row in cur:
    print(row)

cur.close()
conn.close()