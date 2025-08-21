import sqlite3
from lib.db import CONN, CURSOR


class RestGroup:

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
    def get_all(cls):
        CURSOR.execute("SELECT * FROM rest_groups")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM rest_groups WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM rest_groups WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None
    
    @classmethod
    def create(cls, name):
        existing = cls.find_by_name(name)
        if existing:
            return existing
        rest_group = cls(name)
        rest_group.save()
        return rest_group
    
    def restaurants(self):
        from lib.restaurant import Restaurant
        CURSOR.execute("SELECT * FROM restaurants WHERE rest_group_id = ?", (self.id,))
        rows = CURSOR.fetchall()
        return [Restaurant._from_db_row(row) for row in rows] if rows else []

    
    def add_restaurant(self, name, location):
        from lib.restaurant import Restaurant
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

    @classmethod
    def delete(cls, id):
        CURSOR.execute("DELETE FROM rest_groups WHERE id = ?", (id,))
        CONN.commit()

    def save(self):
        CURSOR.execute("INSERT INTO rest_groups (name) VALUES (?)", (self._name,))
        self.id = CURSOR.lastrowid
        CONN.commit()


        