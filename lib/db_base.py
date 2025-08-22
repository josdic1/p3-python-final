import sqlite3
from .db import CONN, CURSOR

class DBBase:
    """A base class for database-related models."""
    _table_name = None

    @classmethod
    def _from_db_row(cls, row):
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def get_all(cls):
        CURSOR.execute(f"SELECT * FROM {cls._table_name}")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute(f"SELECT * FROM {cls._table_name} WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute(f"SELECT * FROM {cls._table_name} WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None

    @classmethod
    def delete(cls, id):
        CURSOR.execute(f"DELETE FROM {cls._table_name} WHERE id = ?", (id,))
        CONN.commit()