"""
main.py - Week 3 Starter

Menu-driven point-of-sale program.

Flow:
1. Welcome banner
2. Ask for customer name, create an Order
3. Show the drink menu, let the customer pick a drink and size
4. Build a MenuItem and add it to the order
5. Show: add another drink / remove a drink / view order / check out
6. On checkout, print the formatted receipt
"""

from menu_item import MenuItem
from order import Order

DRINKS = [
    ("Americano", 3.50),
    ("Cappuccino", 4.25),
    ("Espresso", 3.00),
    ("Latte", 4.75),
]

SIZES = [
    ("Small", 0.00),
    ("Medium", 0.75),
    ("Large", 1.25),
]


def show_drink_menu():
    # TODO: print the drink list with numbers and prices
    print("\n--- Drink Menu ---")
    for i, (name, price) in enumerate(DRINKS, 1):
        print(f"{i}. {name} - ${price:.2f}")


def show_size_menu():
    # TODO: print the size list with numbers and upcharges
    print("\n--- Size ---")
    for i, (size, upcharge) in enumerate(SIZES, 1):
        print(f"{i}. {size} + ${upcharge:.2f}")


def choose_drink():
    """Prompt for a drink and size, return a new MenuItem."""
    # TODO: show drink menu, get choice (1-4)
    drink_choice = int(input("Choose a drink (1-4): "))
    name, base_price = DRINKS[drink_choice - 1]

    # TODO: show size menu, get choice (1-3)
    show_size_menu()
    size_choice = int(input("Choose a size (1-3): "))
    size, upcharge = SIZES[size_choice - 1]

    # TODO: compute price = base + upcharge
    price = base_price + upcharge

    # TODO: return MenuItem(name, size, price)
    return MenuItem(name, size, price)


def main():
    # TODO: print welcome banner
    print("********************************************")
    print("* STARLIGHT COFFEE POS *")
    print("********************************************")

    # TODO: ask for customer name and create an Order
    name = input("Enter your name: ")
    order = Order(name)

    # TODO: add the first drink
    item = choose_drink()
    order.add_item(item)
    print(f"Added: {item}")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add another drink")
        print("2. Remove a drink")
        print("3. View order")
        print("4. Check out")

    # TODO: loop showing the action menu (add / remove / view / check out)
    #       until the user checks out

    # TODO: on checkout, print the order (uses Order.__str__)
        choice = input("Choice: ")

        if choice == "1":
            item = choose_drink()
            order.add_item(item)
            print(f"Added: {item}")

        elif choice == "2":
            print(order)
            index = int(input("Enter item number to remove: "))
            order.remove_item(index)

        elif choice == "3":
            print(order)

        elif choice == "4":
            print(order)
            print(f"Thank you, {name}! Enjoy your coffee.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
