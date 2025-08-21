from cli.groups_cli import groups_menu
from cli.restaurants_cli import restaurants_menu

def run():
    while True:
        print("\n=== Main Menu ===")
        print("1. Restaurant Groups")
        print("2. Restaurants")
        print("3. Exit")

        choice = input("> ").strip()
        if choice == "1":
            groups_menu()
        elif choice == "2":
            restaurants_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    run()