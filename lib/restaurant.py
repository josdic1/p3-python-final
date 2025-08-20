import sqlite3
from lib.db import CONN, CURSOR

class Restaurant:

    all = []

    def __init__(self, name, location, rest_group_id, id = None):
        self.id = id
        self.name = name
        self.location = location
        self.rest_group_id = rest_group_id

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
        if value is None or (isinstance(value, str) and value.strip()):
            self._location = value if value and value.strip() else None
        else:
            raise ValueError("Location must be a string or None")

        
    @property
    def rest_group_id(self):
        return self._rest_group_id
    
    @rest_group_id.setter
    def rest_group_id(self, value):
        if isinstance (value, int) and value > 0:
            self._rest_group_id = value
        else:
            raise ValueError("rest_group_id must be a number")
        
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
    def find_by_name_and_location(cls, name, location):
        CURSOR.execute("SELECT * FROM restaurants WHERE name = ? AND location = ?", (name, location,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None

    @classmethod
    def find_exact_by_name(cls, name, location, rest_group_id):
        if location is None:
            CURSOR.execute("SELECT * FROM restaurants WHERE name = ? AND location IS NULL AND rest_group_id = ?", (name, rest_group_id,))
        else:
            CURSOR.execute("SELECT * FROM restaurants WHERE name = ? AND location = ? AND rest_group_id = ?", (name, location, rest_group_id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None

    @classmethod
    def input_name_output_id(cls, name, location, rest_group_id):
        r = cls.find_exact_by_name(name, location, rest_group_id)
        return r.id if r else None
        
    
    @classmethod
    def create(cls, name, location, rest_group_id):
        existing = cls.find_exact_by_name(name, location, rest_group_id)
        if existing:
            return existing
        restaurant = cls(name, location, rest_group_id)
        restaurant.save()
        return restaurant
    
    def get_related_group(self):
        from lib.rest_group import RestGroup
        rest_group_id = self._group_id
        related_rest_group = RestGroup.find_by_id(rest_group_id)
        return related_rest_group
    
    def update(self):
        CURSOR.execute("UPDATE restaurants SET name = ?, location = ?,rest_group_id = ? WHERE id = ?", (self._name, self._location, self._rest_group_id, self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM restaurants WHERE id = ?", (self.id,))
        CONN.commit()

    def save(self):
        try:
            CURSOR.execute("INSERT INTO restaurants (name, location,rest_group_id) VALUES (?,?,?)", (self.name, self.location, self.rest_group_id))
            self.id = CURSOR.lastrowid
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Unable to save this record")


        