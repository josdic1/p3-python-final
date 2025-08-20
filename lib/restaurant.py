import sqlite3
from .db import CONN, CURSOR

class Restaurant:

    all = []

    def __init__(self, name, group_id, location, id = None):
        self.id = id
        self.name = name
        self.group_id = group_id
        self.location = location

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance (value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name cannot be empty or a duplicate")
        
    @property
    def group_id(self):
        return self._group_id
    
    @group_id.setter
    def group_id(self, value):
        if isinstance (value, int) and value > 0:
            self._group_id = value
        else:
            raise ValueError("group_id cannot be empty or a duplicate")
        
    @classmethod
    def _from_db_row(cls, row):
        group = cls(row[1])
        group.id = (row[0])
        return group
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM groups")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM groups WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM groups WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None
    
    @classmethod
    def create(cls, name):
        existing = cls.find_by_name(name)
        if existing:
            return existing
        group = cls(name)
        group.save()
        return group
    
    def update(self):
        CURSOR.execute("UPDATE group SET name = ? WHERE id = ?", (self._name,self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM groups WHERE id = ?", (self.id,))
        CONN.commit()

    def save(self):
        CURSOR.execute("INSERT INTO groups (name) VALUES (?)", (self._name,))
        self.id = self.id
        CONN.commit()


        