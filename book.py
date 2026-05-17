from library_item import LibraryItem


class Book(LibraryItem):

    def __init__(self, title, author, year, isbn, page_count, checked_out=False):
        super().__init__(title, author, year, checked_out)
        self.isbn = isbn
        self.page_count = int(page_count)

    def get_item_type(self):
        return "Book"

    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"ISBN: {self.isbn}, Pages: {self.page_count}"
        )