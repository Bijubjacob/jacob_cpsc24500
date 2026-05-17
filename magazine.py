"""
magazine.py - Week 8 Starter

Magazine extends LibraryItem with issue_number (int) and month (str).
"""

from library_item import LibraryItem


class Magazine(LibraryItem):

    def __init__(self, title, author, year, issue_number, month, checked_out=False):
        super().__init__(title, author, year, checked_out)
        self.issue_number = int(issue_number)
        self.month = month

    def get_item_type(self):
        return "Magazine"

    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Issue: {self.issue_number}, Month: {self.month}"
        )