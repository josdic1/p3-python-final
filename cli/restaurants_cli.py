from lib.restaurant import Restaurant
from lib.rest_group import RestGroup

def restaurants_menu():
    while True:
        print("\n=== Restaurants ===")
        restaurants = Restaurant.get_all()
        for i, r in enumerate(restaurants, start=1):
            print(f"{i}. {r.name} - {r.location}")

        print("\nActions: S=search, N=new, D=delete, B=back, X=exit")
        choice = input("> ").strip().upper()

        if choice == "B":
            return
        elif choice == "X":
            print("Goodbye")
            return 
        elif choice == "N":
            print("Restaurants must be created from a parent group")
        elif choice == "D":
            delete_restaurant()
        elif choice == "S":
            search_by_name()
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(restaurants):
                view_restaurant(restaurants[index].id)
            else:
                print("Invalid selection")

def search_by_name():
    name = input("Enter restaurant name: ").strip()
    r = Restaurant.find_by_name(name)
    if r:
        view_restaurant(r.id)
    else:
        print("No match")

def delete_restaurant():
    restaurants = Restaurant.get_all()
    for i, r in enumerate(restaurants, start=1):
        print(f"{i}. {r.name} - {r.location}")
    choice = input("Enter number to delete: ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(restaurants):
            Restaurant.delete(restaurants[index].id)
            print(f"Deleted {restaurants[index].name}")

def view_restaurant(restaurant_id):
    r = Restaurant.find_by_id(restaurant_id)
    if not r:
        print("No restaurant found")
        return
    g = RestGroup.find_by_id(r.rest_group_id)
    print(f"\n=== {r.name} ===")
    print(f"Location: {r.location}")
    print(f"Parent Group: {g.name if g else 'None'}")

    while True:
        choice = input("B=back, X=exit > ").strip().upper()
        if choice == "B":
            return
        elif choice == "X":
            exit()
