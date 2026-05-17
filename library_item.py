"""
library_item.py - Week 8 Starter

LibraryItem is the abstract base class for all catalog items.

Attributes (private with @property):
- title (str)
- author (str)
- year (int)
- checked_out (bool)

Abstract:
- get_item_type() -> str  (subclasses return "Book", "DVD", or "Magazine")

Concrete:
- check_out(): raise RuntimeError if already checked out
- check_in(): raise RuntimeError if already available
- __lt__: sort by title, case-insensitive
- __str__: includes type, title, author, year, status
"""

from abc import ABC, abstractmethod


from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def __init__(self, title, author, year, checked_out=False):
        self._title = title
        self._author = author
        self._year = int(year)
        self._checked_out = checked_out

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def checked_out(self):
        return self._checked_out

    @abstractmethod
    def get_item_type(self):
        pass

    def check_out(self):
        if self._checked_out:
            raise RuntimeError("Item already checked out.")
        self._checked_out = True

    def check_in(self):
        if not self._checked_out:
            raise RuntimeError("Item already available.")
        self._checked_out = False

    def __lt__(self, other):
        return self.title.lower() < other.title.lower()

    def __str__(self):
        status = "CHECKED OUT" if self.checked_out else "AVAILABLE"

        return (
            f"[{self.get_item_type()}] "
            f"{self.title} by {self.author} "
            f"({self.year}) - {status}"
        )