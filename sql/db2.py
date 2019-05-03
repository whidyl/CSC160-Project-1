import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
    ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
    ('My Way', 15))
conn.commit()

print('Tracks:')
cur.execute('SELECT * FROM Tracks')
for row in cur:
     print(row)

cur.execute('DELETE FROM Tracks')
conn.commit()

cur.close()
