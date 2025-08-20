# lib/cli.py
from lib.rest_group import RestGroup
from lib.restaurant import Restaurant

def run():
    while True:
        print("\nMain Menu")
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
    all = RestGroup.get_all()
    for rg in all:
        print(f"{rg.id}: {rg.name}")
    choice = input("Enter group id to view, or B to go back: ")

    if choice.upper() == "B":
        print("\nReturning to main menu")
        return

    elif choice.isdigit():
        group = RestGroup.find_by_id(int(choice))
        if group:
            for r in group.restaurants():
                print(f"{r.id}: {r.name}")
            choice = input("Enter restaurant id to view, or B to go back: ")

            if choice.upper() == "B":
                print("\nReturning to main menu")
                return

        else:
            print("No group found with that id.")
    else:
        print("Invalid choice")

def restaurants_menu():
    print("TODO: restaurants submenu")

if __name__ == "__main__":
    run()
