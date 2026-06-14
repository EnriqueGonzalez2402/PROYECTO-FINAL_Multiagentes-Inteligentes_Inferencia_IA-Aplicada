# ver_historial.py

import sqlite3

conn = sqlite3.connect("aura.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM historial")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()