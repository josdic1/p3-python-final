# lib/cli.py
from lib.rest_group import RestGroup
from lib.restaurant import Restaurant


def run():
    while True:
        print("\n=== Main Menu ===")
        print("1. Restaurant Groups")
        print("2. Restaurants")
        print("3. Exit")

        choice = input("> ")

        if choice == "1":
            groups_menu()
        elif choice == "2":
            restaurants_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


def groups_menu():
    while True:
        print("\n=== Restaurant Groups ===")
        all = RestGroup.get_all()
        for rg in all:
            print(f"{rg.id}: {rg.name}")  

        print("\n=== Actions ===")
        print("Enter DB ID# to view restaurants")
        print("N = new, D = delete, B = back")

        choice = input("> ")
        if choice.upper() == "N":
            create_group()
        elif choice.upper() == "D":
            delete_group()
        elif choice.upper() == "B":
            return
        elif choice.isdigit():
            view_group(int(choice))


def create_group():
    print("\n=== New Restaurant Group ===")
    name = input("Enter new group name: ")

    new_group = RestGroup.create(name)
    print(f"Created new group: {new_group.id} - {new_group.name}")
    

def delete_group():
    print("\n=== Choose group to delete ===")
    all = RestGroup.get_all()
    for rg in all:
        print(f"{rg.id}: {rg.name}")

    print("\n=== DELETE Restaurant Group ===")
    id_str = input("Enter group id to delete: ")

    if id_str.isdigit():
        id = int(id_str)
        RestGroup.delete(id)
        print(f"{id} has been deleted")
    else:
        print("Invalid ID")


def view_group(group_id):
    group = RestGroup.find_by_id(group_id)
    if not group:
        print("No group found with that ID")
        return

    while True:
        print(f"\n=== Restaurants in {group.name} ===")
        restaurants = group.restaurants()
        for r in restaurants:
            print(f"{r.id}. {r.name}")

        print("\nOptions: N = new restaurant, B = back")
        choice = input("> ")

        if choice.upper() == "B":
            return
        elif choice.upper() == "N":
            print("\n=== Creating new restaurant ===")
            name = input("Enter restaurant name: ")
            location = input("Enter restaurant location: ")

            new_restaurant = group.add_restaurant(name, location)
            print(f"Created new retaurant: {new_restaurant.id} - {new_restaurant.name} in {new_restaurant.location} in {group.name}")


def restaurants_menu():
    pass


if __name__ == "__main__":
    run()
