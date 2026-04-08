"""
menu_item.py - Week 3 Starter

The MenuItem class represents a single item on the coffee shop menu.

Attributes:
- name (str): drink name (e.g., "Latte")
- size (str): "Small", "Medium", or "Large"
- price (float): final price (base price + size upcharge)

Methods:
- __str__: returns a string like "Latte (Large) - $6.00"
"""


class MenuItem:

    def __init__(self, name, size, price):
        # TODO: store name, size, and price as instance attributes
        self.name = name
        self.size = size
        self.price = price

    def __str__(self):
        # TODO: return a string in the format "Latte (Large) - $6.00"
        # Hint: f"{self.name} ({self.size}) - ${self.price:.2f}"
        return f"{self.name} ({self.size}) - ${self.price:.2f}"
