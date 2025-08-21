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
        for i, rg in enumerate(all, start=1):
            print(f"{i}. {rg.name}")

        print("\n=== Actions ===")
        print("Enter DB ID# to view restaurants")
        print("S = Search by name, N = new, D = delete, B = back, X = exit")
        
        choice = input("> ")

        if choice.upper() == "N":
            create_group()
        elif choice.upper() == "D":
            delete_group()
        elif choice.upper() == "B":
            return
        elif choice.upper() == "S":
            search_by_name()
        elif choice.isdigit():
            index = int(choice) - 1
        if 0 <= index < len(all):
            group = all[index]
            view_group(group.id)
        else:
            print("Invalid choice")


def search_by_name():
    print("\n=== Search Restaurant Groups by Name ===")
    name = input("Enter group name: ").strip() or None

    if name:
        group = RestGroup.find_by_name(name)
        if group:
            print(f"MATCH FOUND! {group.name}")
            view_group(group.id)
        else:
            print(f"NO MATCH FOUND!")

def create_group():
    print("\n=== New Restaurant Group ===")
    name = input("Enter new group name: ")

    new_group = RestGroup.create(name)
    print(f"Created new group: {new_group.id} - {new_group.name}")
    

def delete_group():
    print("\n=== Choose group to delete ===")
    all = RestGroup.get_all()
    for i, rg in enumerate(all, start=1):
        print(f"{i}. {rg.name}")

    print("\n=== DELETE Restaurant Group ===")
    choice = input("Enter number to delete: ")

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(all):
            group = all[index]
            RestGroup.delete(group.id)
            print(f"{group.name} has been deleted")
        else:
            print("Invalid selection")
    else:
        print("Invalid input")


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

        print("\nOptions: N = new restaurant, B = back, X = exit")
        choice = input("> ")

        if choice.upper() == "B":
            return
        elif choice.upper() == "X":
            print("Goodbye!")
            exit()
        elif choice.upper() == "N":
            print("\n=== Creating new restaurant ===")
            name = input("Enter restaurant name: ")
            location = input("Enter restaurant location: ")

            new_restaurant = group.add_restaurant(name, location)
            print(f"Created new retaurant: {new_restaurant.id} - {new_restaurant.name} in {new_restaurant.location} in {group.name}")


def restaurants_menu():
    while True:
        print("\n=== Restaurants ===")
        all = Restaurant.get_all()
        for i, r in enumerate(all, start=1):
            print(f"{i}. {r.name} - {r.location}")

        print("\n=== Actions ===")
        print("Enter number to view restaurant")
        print("S = search by location, N = new, D = delete, B = back, X = exit")

        choice = input("> ")
        if choice.upper() == "N":
            new_restaurant_reroute()
        elif choice.upper() == "D":
            delete_restaurant()
        elif choice.upper() == "S":
            search_by_name()
        elif choice.upper() == "B":
            return
        elif choice.upper() == "X":
            print("Goodbye!")
            exit()
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(all):
                restaurant = all[index]
                view_restaurant(restaurant.id)
            else:
                print("Invalid selection")
        else:
            print("Invalid input")

def search_by_name():
    print("\n=== Search by Restaurant name ===")
    name = input("Enter restaurant name: ").strip() or None

    if name:
        restaurant = Restaurant.find_by_name(name)
        if restaurant:
            print(f"MATCH FOUND! {restaurant.name}")
            view_restaurant(restaurant.id)
        else:
            print(f"NO MATCH FOUND!")

def new_restaurant_reroute():
    print("You must select a parent restaurant group BEFORE creating a new restaurant")
    print("\nI. Choose a parent restaurant group")
    print("II. Enter the parent restaurant group ID# (i.e. '==> 1: YUM! Brands')")
    print("III. Select 'N' to add a new restaurant to the group")
    groups_menu()

def delete_restaurant():
    print("\n=== Choose restaurant to delete ===")
    all = Restaurant.get_all()
    for i, r in enumerate(all, start=1):
        print(f"{i}. {r.name} - {r.location}")

    print("\n=== DELETE Restaurant ===")
    choice = input("Enter number to delete: ")

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(all):
            restaurant = all[index]
            Restaurant.delete(restaurant.id)
            print(f"{restaurant.name} has been deleted")
        else:
            print("Invalid selection")
    else:
        print("Invalid input")

def view_restaurant(restaurant_id):
    while True:
        restaurant = Restaurant.find_by_id(restaurant_id)
        if restaurant:
            group = RestGroup.find_by_id(restaurant.rest_group_id)
    
        if group:
            print(f"\n=== {restaurant.name} ===")
            print(f"Location: {restaurant.location}")
            print(f"Parent Group: {group.name}")


            print("\nOptions: B = back, X = exit")
            choice = input("> ")

        if choice.upper() == "B":
            return
        elif choice.upper() == "X":
            print("Goodbye!")
            exit()
        else:
            print("Invalid ID")

if __name__ == "__main__":
    run()
