import sqlite3

CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

SQL_DROP = """
DROP TABLE IF EXISTS restaurants;
DROP TABLE IF EXISTS groups;
"""

SQL_DELETE = """
CURSOR.execute("DELETE FROM restaurants")
CURSOR.execute("DELETE FROM rest_groups")
CONN.commit()
"""

CURSOR.executescript(SQL_DROP)
CONN.commit()

print("❌ Tables dropped.")
