from lib.rest_group import RestGroup
from cli.restaurants_cli import view_restaurant

def groups_menu():
    while True:
        print("\n=== Restaurant Groups ===")
        groups = RestGroup.get_all()
        for i, g in enumerate(groups, start=1):
            print(f"{i}. {g.name}")

        print("\nActions: S=search, N=new, D=delete, B=back, X=exit")
        choice = input("> ").strip().upper()

        if choice == "B":
            return
        elif choice == "X":
            print("Goodbye!")
            exit()
        elif choice == "N":
            create_group()
        elif choice == "D":
            delete_group()
        elif choice == "S":
            search_by_name()
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(groups):
                view_group(groups[index].id)
            else:
                print("Invalid selection")
        else:
            print("Invalid input")

def create_group():
    name = input("Enter new group name: ")
    new_group = RestGroup.create(name)
    print(f"Created group: {new_group.name}")

def delete_group():
    groups = RestGroup.get_all()
    for i, g in enumerate(groups, start=1):
        print(f"{i}. {g.name}")
    choice = input("Enter number to delete: ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(groups):
            RestGroup.delete(groups[index].id)
            print(f"Deleted {groups[index].name}")
    else:
        print("Invalid input")

def search_by_name():
    name = input("Enter group name: ").strip()
    group = RestGroup.find_by_name(name)
    if group:
        print(f"Match: {group.name}")
        view_group(group.id)
    else:
        print("No match")

def view_group(group_id):
    group = RestGroup.find_by_id(group_id)
    if not group:
        print("No group found")
        return

    while True:
        print(f"\n=== Restaurants in {group.name} ===")
        restaurants = group.restaurants()
        for i, r in enumerate(restaurants, start=1):
            print(f"{i}. {r.name}")

        print("\nOptions: N=new, B=back, X=exit")
        choice = input("> ").strip().upper()

        if choice == "B":
            return
        elif choice == "X":
            exit()
        elif choice == "N":
            name = input("Restaurant name: ")
            location = input("Location: ")
            new_r = group.add_restaurant(name, location)
            print(f"Created {new_r.name} in {new_r.location}")
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(restaurants):
                view_restaurant(restaurants[index].id)
            else:
                print("Invalid selection")
