import sqlite3

CONN = sqlite3.connect('database.db')
CURSOR = CONN.cursor()
CURSOR.execute("PRAGMA foreign_keys = ON;")

SCHEMA = """
CREATE TABLE IF NOT EXISTS rest_groups (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT,
    rest_group_id INTEGER NOT NULL,
    FOREIGN KEY (rest_group_id) REFERENCES rest_groups(id) ON DELETE CASCADE,
    UNIQUE(name, location, rest_group_id)
);
"""

CURSOR.executescript(SCHEMA)
CONN.commit()

print("✅ Tables ready")