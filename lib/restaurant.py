import sqlite3
from lib.db import CONN, CURSOR

class Restaurant:

    all = []

    def __init__(self, name, location, group_id, id = None):
        self.id = id
        self.name = name
        self.location = location
        self.group_id = group_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance (value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name cannot be empty")
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        if isinstance (value, str) and value.strip():
            self._location = value
        else:
            raise ValueError("No location added")

        
    @property
    def group_id(self):
        return self._group_id
    
    @group_id.setter
    def group_id(self, value):
        if isinstance (value, int) and value > 0:
            self._group_id = value
        else:
            raise ValueError("group_id must be a number")
        
    @classmethod
    def _from_db_row(cls, row):
        restaurant = cls(row[1], row[2], row[3])
        restaurant.id = (row[0])
        return restaurant
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM restaurants")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM restaurants WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM restaurants WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None
    
    @classmethod
    def create(cls, name, location, group_id):
        existing = cls.find_by_name(name)
        if existing:
            return existing
        restaurant = cls(name, location, group_id)
        restaurant.save()
        return restaurant
    
    def get_related_group(self):
        from lib.group import Group
        my_group_id = self._group_id
        related_group = Group.find_by_id(my_group_id)
        return related_group
    
    def update(self):
        CURSOR.execute("UPDATE restaurants SET name = ?, location = ?, group_id = ? WHERE id = ?", (self._name, self._location, self._group_id, self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM restaurants WHERE id = ?", (self.id,))
        CONN.commit()

    def save(self):
        try:
            CURSOR.execute("INSERT INTO restaurants (name, location, group_id) VALUES (?,?,?)", (self.name, self.location, self.group_id))
            self.id = CURSOR.lastrowid
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Unable to save this record")


        