"""
catalog_view.py - Week 8 Starter

The View handles ALL display and output formatting. It does not store data
and does not modify the catalog.

Keep this class focused on printing. Anything that creates or modifies items
belongs in main.py (the controller).
"""


class CatalogView:

    def display_items(self, items):

        if not items:
            print("No items to display.")
            return

        for item in items:
            print(item)

    def display_message(self, message):
        print(message)

    def display_menu(self):

        print("\n=============================")
        print("Library Catalog System")
        print("=============================")
        print("1. List all items")
        print("2. Search by title")
        print("3. Search by author")
        print("4. Check out item")
        print("5. Check in item")
        print("6. Add new item")
        print("7. View checked-out items")
        print("8. Save and quit")

    def display_search_results(self, items, query):

        print(f'\n--- Search Results for "{query}" ---')

        self.display_items(items)