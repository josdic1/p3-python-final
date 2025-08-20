from lib.db import CONN, CURSOR
from lib.rest_group import RestGroup
from lib.restaurant import Restaurant

def seed():
    # clear old data
    CURSOR.execute("DELETE FROM restaurants")
    CURSOR.execute("DELETE FROM rest_groups")
    CONN.commit()

    # groups
    yum = RestGroup.create("YUM! Brands")
    darden = RestGroup.create("Darden Restaurants")
    bloomin = RestGroup.create("Bloomin' Brands")
    brinker = RestGroup.create("Brinker International")
    cheesecake = RestGroup.create("Cheesecake Factory Inc.")
    denny = RestGroup.create("Denny’s Corp.")
    ihop = RestGroup.create("Dine Brands (IHOP/Applebee’s)")
    shake = RestGroup.create("Shake Shack Inc.")
    chipotle = RestGroup.create("Chipotle Mexican Grill")
    wingstop = RestGroup.create("Wingstop Inc.")

    # restaurants (30 total, 3 per group)
    Restaurant.create("KFC", "Louisville, KY", yum.id)
    Restaurant.create("Taco Bell", "Irvine, CA", yum.id)
    Restaurant.create("Pizza Hut", "Plano, TX", yum.id)

    Restaurant.create("Olive Garden", "Orlando, FL", darden.id)
    Restaurant.create("LongHorn Steakhouse", "Orlando, FL", darden.id)
    Restaurant.create("Seasons 52", "Orlando, FL", darden.id)

    Restaurant.create("Outback Steakhouse", "Tampa, FL", bloomin.id)
    Restaurant.create("Carrabba’s Italian Grill", "Tampa, FL", bloomin.id)
    Restaurant.create("Bonefish Grill", "Tampa, FL", bloomin.id)

    Restaurant.create("Chili’s", "Dallas, TX", brinker.id)
    Restaurant.create("Maggiano’s Little Italy", "Dallas, TX", brinker.id)
    Restaurant.create("Italianni’s", "Mexico City", brinker.id)

    Restaurant.create("The Cheesecake Factory", "Calabasas, CA", cheesecake.id)
    Restaurant.create("North Italia", "Austin, TX", cheesecake.id)
    Restaurant.create("Flower Child", "Phoenix, AZ", cheesecake.id)

    Restaurant.create("Denny’s", "Spartanburg, SC", denny.id)
    Restaurant.create("Denny’s Diner Classic", "Las Vegas, NV", denny.id)
    Restaurant.create("Denny’s Express", "Los Angeles, CA", denny.id)

    Restaurant.create("IHOP", "Glendale, CA", ihop.id)
    Restaurant.create("Applebee’s", "Glendale, CA", ihop.id)
    Restaurant.create("IHOP Express", "New York, NY", ihop.id)

    Restaurant.create("Shake Shack", "New York, NY", shake.id)
    Restaurant.create("Shake Shack Madison", "New York, NY", shake.id)
    Restaurant.create("Shake Shack Tokyo", "Tokyo, Japan", shake.id)

    Restaurant.create("Chipotle Mexican Grill", "Denver, CO", chipotle.id)
    Restaurant.create("Chipotle UK", "London, UK", chipotle.id)
    Restaurant.create("Chipotle Canada", "Toronto, ON", chipotle.id)

    Restaurant.create("Wingstop", "Dallas, TX", wingstop.id)
    Restaurant.create("Wingstop UK", "London, UK", wingstop.id)
    Restaurant.create("Wingstop Mexico", "Monterrey, MX", wingstop.id)

    print("✅ Database seeded with 10 groups and 30 restaurants")

    print("\nGroups:")
    for g in RestGroup.get_all():
        print(g)

    print("\nRestaurants:")
    for r in Restaurant.get_all():
        print(r)

if __name__ == "__main__":
    seed()