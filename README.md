

## Phase 3: Restaurant Groups CLI

This is a command-line interface (CLI) application for managing restaurant groups and the restaurants they own. You can add, search for, and delete both groups and restaurants directly from the terminal.

⚠️ **NOTE:** This project was built from scratch to better understand CLI and database design.

### How to Use

Run the application with: `python main.py`

Navigate through the menus using the provided options to manage groups and restaurants.

### Files

* `main.py`: The entry point for the application.
* `lib/db_base.py`: Defines a base class for database models. This class handles common database operations, such as fetching and deleting records, and is inherited by other classes to reduce code duplication.
* `lib/rest_group.py`: Defines the `RestGroup` class, which represents a group of restaurants. It inherits from `DBBase` and includes methods to manage groups and their associated restaurants.
* `lib/restaurant.py`: Defines the `Restaurant` class, which represents a single restaurant. It inherits from `DBBase` and includes methods to manage restaurant records.
* `lib/db.py`: Establishes the connection to the SQLite database.
* `drop_tables.py`: A utility script to reset the database by deleting all tables.
* `cli/groups_cli.py`: Contains the menu and functions for group-related actions.
* `cli/restaurants_cli.py`: Contains the menu and functions for restaurant-related actions.

### Notes

* Written in Python 3.8 and uses SQLite for the database.