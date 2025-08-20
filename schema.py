import sqlite3

CONN = sqlite3.connect('database.db')
CURSOR = CONN.cursor()



CURSOR.executescript()
CONN.commit()
CONN.close()

print("✅ Tables created from schema.")