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
    print("\n=== Restaurant Groups ===")
    all = RestGroup.get_all()
    for rg in all:
        print(f"{rg.id}: {rg.name}")

    choice = input("\nEnter group id to view, N to create new group, or B to go back: ")

    if choice.upper() == "B":
        return

    elif choice.upper() == "N":
        print("\n=== New Restaurant Group ===")
        name = input("Enter new group name: ")

        new_group = RestGroup.create(name)
        print(f"\nCreated new group: {new_group.id} - {new_group.name}")
        
    elif choice.isdigit():
        group = RestGroup.find_by_id(int(choice))
        if group:
            restaurants_in_group(group)
        else:
            print("No group found with that id.")
    else:
        print("Invalid choice")


def restaurants_in_group(group):
    print(f"\n=== Restaurants in {group.name} ===")
    for r in group.restaurants():
        print(f"{r.id}: {r.name}")

    choice = input("Enter restaurant id to view, N to create/assign restaurant to this goup, or B to go back: ")

    if choice.upper() == "B":
        return
    elif choice.isdigit():
        restaurant = Restaurant.find_by_id(int(choice))
        if restaurant:
            show_restaurant(restaurant)
        else:
            print("No restaurant found with that id.")
    else:
        print("Invalid choice")


def show_restaurant(restaurant):
    print(f"\n--- Restaurant ---")
    print(f"ID: {restaurant.id}")
    print(f"Name: {restaurant.name}")
    input("\nPress Enter to go back...")


def restaurants_menu():
    print("\n=== All Restaurants ===")
    all = Restaurant.get_all()
    for r in all:
        print(f"{r.id}: {r.name}")

    choice = input("Enter restaurant id to view, or B to go back: ")

    if choice.upper() == "B":
        return
    elif choice.isdigit():
        restaurant = Restaurant.find_by_id(int(choice))
        if restaurant:
            restaurant_selection(restaurant)
        else:
            print("No restaurant found with that ID.")
    else:
        print("Invalid choice")


def restaurant_selection(restaurant):
    print(f"\n--- Restaurant ---")
    print(f"ID: {restaurant.id}")
    print(f"Name: {restaurant.name}")
    input("\nPress Enter to go back...")


if __name__ == "__main__":
    run()
