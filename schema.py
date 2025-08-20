import sqlite3

CONN = sqlite3.connect('database.db')
CURSOR = CONN.cursor()

SCHEMA = """

CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    location TEXT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups.id
);

"""

CURSOR.executescript(SCHEMA)
CONN.commit()
CONN.close()

print("✅ Tables created from schema.")