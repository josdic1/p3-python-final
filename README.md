
# Phase 3: Restaurant Groups CLI

This is my Phase 3 CLI project. It’s a command line application where you can manage restaurant groups and the restaurants that belong to them. You can add new groups, add restaurants to a group, search, and delete items all from the terminal. 

⚠️ PLEASE NOTE ⚠️                           
*I did not use the template provided in the Phase 3 final repo. I attempted to write my own cli in order to better understand it.*

## How to Use
Run the CLI with:
```main.py```
Runs the whole program.  
```python
from cli.main import run

if __name__ == "__main__":
    run()
```    
### Use the menus to navigate:

- **Main menu** lets you choose Groups or Restaurants  
  - In **groups**, you can view restaurants inside, create a new group, search by name, or delete a group  
    - In **restaurants**, you can see all restaurants, search, or delete  


## Files

```python main.py``` This runs the CLI or main entry point. It prints menus, takes user input, and calls functions for creating, searching, and deleting.

```lib/rest_group.py``` 
Defines the **RestGroup** class. Represents a restaurant group (like **YUM! Brands**, owner of Taco Bell, KFC, Pizza Hut, etc).  

*The Restaurant Group is the PARENT of a CHILD Restaurant*

Attributes: `id`, `name`.  
Methods:  
- `get_all()` → returns all groups  
- `find_by_id()` → find a group by its id  
- `create()` → add a new group  
- `delete()` → remove a group  
- `.restaurants()` → see all restaurants that belong to this group  

```lib/restaurant.py```
Defines the Restaurant class and represents one restaurant. 

#### Attributes: 
```id```, ```name```, ```location```, ```rest_group_id```. 

Includes methods to ```get all``` restaurants, ```find by id```, ```find by name```, ```create```, ```delete```. It also has a ```get_related_group(self)``` method that returns a restaurants corresponding **RestGroup**.

```lib/db.py```
Sets up the database connection with SQLite. Provides CONN and CURSOR that the models use for queries.

```drop_tables.py```
Utility script to clear out the database. It drops the restaurants and groups tables and commits changes. Run this if you want to reset everything.

### CLI
```cli/main.py```
Contains the run() function and main menu loop.

```cli/groups_cli.py```
Functions for group-related menus and actions.

```cli/restaurants_cli.py```
Functions for restaurant-related menus and actions.

## Notes

- Written with Python 3.8, SQLite