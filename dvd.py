"""
dvd.py - Week 8 Starter

DVD extends LibraryItem with runtime_minutes (int) and rating (str).
"""

from library_item import LibraryItem


class DVD(LibraryItem):

    def __init__(self, title, author, year, runtime_minutes, rating, checked_out=False):
        super().__init__(title, author, year, checked_out)
        self.runtime_minutes = int(runtime_minutes)
        self.rating = rating

    def get_item_type(self):
        return "DVD"

    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Runtime: {self.runtime_minutes} min, Rating: {self.rating}"
        )