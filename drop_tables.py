import sqlite3

CONN = sqlite3.connect('database.db')
CURSOR = CONN.cursor

SQL = """
DROP TABLE IF EXISTS restaurants;
DROP TABLE IF EXISTS groups;
"""

CURSOR.executescript(SQL)
CONN.commit()

print("❌ Tables dropped.")