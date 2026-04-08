"""
order.py - Week 3 Starter

The Order class represents a customer's order containing one or more MenuItems.

Attributes:
- customer_name (str)
- items (list of MenuItem)

Methods:
- add_item(item): append a MenuItem to the order
- remove_item(index): remove an item by 1-based index
- subtotal(): sum of all item prices
- tax(): subtotal * 0.0875
- total(): subtotal + tax
- __str__: formatted receipt string
"""

from menu_item import MenuItem

TAX_RATE = 0.0875


class Order:

    def __init__(self, customer_name):
        # TODO: store the customer name
        self.customer_name = customer_name

        # TODO: initialize an empty list for items
        self.items = []

    def add_item(self, item):
        # TODO: append the item to self.items
        self.items.append(item)

    def remove_item(self, index):
        # TODO: remove the item at position (index - 1) since the menu shows 1-based numbers
        # Hint: use self.items.pop(index - 1)
        if 1 <= index <= len(self.items):
            self.items.pop(index - 1)
        else:
            print("Invalid item number.")

    def subtotal(self):
        # TODO: return the sum of prices for all items
        return sum(item.price for item in self.items)

    def tax(self):
        # TODO: return self.subtotal() * TAX_RATE
        return self.subtotal() * TAX_RATE

    def total(self):
        # TODO: return subtotal + tax
        return self.subtotal() + self.tax()

    def __str__(self):
        # TODO: build and return a formatted receipt string
        # Include: header, customer name, each item with number, subtotal, tax, total
        receipt = "\n============================================\n"
        receipt += "STARLIGHT COFFEE RECEIPT\n"
        receipt += "============================================\n"
        receipt += f"Customer: {self.customer_name}\n"
        receipt += "--------------------------------------------\n"

        for i, item in enumerate(self.items, 1):
            receipt += f"{i}. {item.name} ({item.size}) - ${item.price:.2f}\n"

        receipt += "--------------------------------------------\n"
        receipt += f"Subtotal: ${self.subtotal():.2f}\n"
        receipt += f"Tax (8.75%): ${self.tax():.2f}\n"
        receipt += f"TOTAL: ${self.total():.2f}\n"
        receipt += "============================================\n"

        return receipt
