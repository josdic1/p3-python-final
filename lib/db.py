import sqlite3

CONN = sqlite3.connect('database.db')
CURSOR = CONN.cursor()
CURSOR.execute("PRAGMA foreign_keys = ON;")

SCHEMA = """
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
    UNIQUE(name, location, group_id)
);
"""

CURSOR.executescript(SCHEMA)
CONN.commit()

print("✅ Tables ready")