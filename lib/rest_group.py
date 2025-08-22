import sqlite3
from .db import CONN, CURSOR
from .db_base import DBBase

class RestGroup(DBBase):
    _table_name = "rest_groups"

    def __init__(self, name, id = None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<RestGroup id={self.id} name='{self.name}'>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance (value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name cannot be empty")
        
    @classmethod
    def _from_db_row(cls, row):
        rest_group = cls(row[1])
        rest_group.id = (row[0])
        return rest_group

    @classmethod
    def create(cls, name):
        existing = cls.find_by_name(name)
        if existing:
            return existing
        rest_group = cls(name)
        rest_group.save()
        return rest_group
    
    def restaurants(self):
        from .restaurant import Restaurant
        CURSOR.execute("SELECT * FROM restaurants WHERE rest_group_id = ?", (self.id,))
        rows = CURSOR.fetchall()
        return [Restaurant._from_db_row(row) for row in rows] if rows else []

    def add_restaurant(self, name, location):
        from .restaurant import Restaurant
        new_restaurant = Restaurant.find_exact_by_name(name, location, self.id)

        if new_restaurant:
            new_restaurant.rest_group_id = self.id
            new_restaurant.update()
            return new_restaurant
        else:
            new_restaurant = Restaurant.create(name, location, self.id)
            return new_restaurant

    def update(self):
        CURSOR.execute("UPDATE rest_groups SET name = ? WHERE id = ?", (self._name,self.id,))
        CONN.commit()

    def save(self):
        CURSOR.execute("INSERT INTO rest_groups (name) VALUES (?)", (self._name,))
        self.id = CURSOR.lastrowid
        CONN.commit()