from lib.db import CONN, CURSOR
from lib.rest_group import RestGroup
from lib.restaurant import Restaurant

def seed():
    CURSOR.execute("DELETE FROM restaurants")
    CURSOR.execute("DELETE FROM rest_groups")
    CONN.commit()

    # groups
    ## give me 10 restaurant groups(i.e. YUM brands, Darden,)

    # restaurants
    ## give me 30 restaurants (with corrresponding rest_hroup

if __name__ == "__main__":
    seed()