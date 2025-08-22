import sqlite3
from .db import CONN, CURSOR
from .db_base import DBBase

class Restaurant(DBBase):
    _table_name = "restaurants"

    def __init__(self, name, location, rest_group_id, id = None):
        self.id = id
        self.name = name
        self.location = location
        self.rest_group_id = rest_group_id

    def __repr__(self):
        return f"<Restaurant id={self.id} name='{self.name}' location='{self.location}' group_id={self.rest_group_id}>"

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
        return cls(id=row[0], name=row[1], location=row[2], rest_group_id=row[3])
    
    # Redundant get_all, find_by_id, find_by_name, and delete methods removed

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
    def create(cls, name, location, rest_group_id):
        existing = cls.find_exact_by_name(name, location, rest_group_id)
        if existing:
            return existing
        restaurant = cls(name, location, rest_group_id)
        restaurant.save()
        return restaurant
    
    def get_related_group(self):
        from .rest_group import RestGroup
        rest_group_id = self._rest_group_id
        related_rest_group = RestGroup.find_by_id(rest_group_id)
        return related_rest_group
    
    def update(self):
        CURSOR.execute("UPDATE restaurants SET name = ?, location = ?,rest_group_id = ? WHERE id = ?", (self._name, self._location, self._rest_group_id, self.id,))
        CONN.commit()

    def save(self):
        try:
            with CONN:
                CURSOR.execute("INSERT INTO restaurants (name, location,rest_group_id) VALUES (?,?,?)", (self.name, self.location, self.rest_group_id))
                self.id = CURSOR.lastrowid
        except sqlite3.IntegrityError:
            print("Unable to save this record")



        