"""
main.py - Week 8 Starter (Controller)

This is the controller. It coordinates the Catalog (model), CatalogView (view),
and ItemFactory (creation).

Flow:
1. Load data/catalog.tsv at startup (use ItemFactory.create_item for each row)
2. Show the menu and read the user's choice
3. Dispatch to the right action; delegate display to CatalogView
4. On "Save and quit", write the catalog back to the file in the same format
5. Wrap risky operations in try/except so the program never crashes

Menu:
1. List all items
2. Search by title
3. Search by author
4. Check out item
5. Check in item
6. Add new item
7. View checked-out items
8. Save and quit
"""

import os
from catalog import Catalog
from catalog_view import CatalogView
from item_factory import ItemFactory

DATA_FILE = os.path.join("data", "catalog.tsv")


def load_catalog(catalog, filename):

    try:
        with open(filename, "r") as file:

            for line in file:

                parts = line.strip().split("\t")

                item_type = parts[0]
                title = parts[1]
                author = parts[2]
                year = int(parts[3])

                checked_out = parts[-1].lower() == "true"

                extras = parts[4:-1]

                item = ItemFactory.create_item(
                    item_type,
                    title,
                    author,
                    year,
                    *extras
                )

                if checked_out:
                    item._checked_out = True

                catalog.add_item(item)

    except FileNotFoundError:
        print("Catalog file not found. Starting empty catalog.")


def save_catalog(catalog, filename):

    with open(filename, "w") as file:

        for item in catalog.get_all_items():

            checked = str(item.checked_out).lower()

            if item.get_item_type() == "Book":

                line = (
                    f"Book\t{item.title}\t{item.author}\t"
                    f"{item.year}\t{item.isbn}\t"
                    f"{item.page_count}\t{checked}\n"
                )

            elif item.get_item_type() == "DVD":

                line = (
                    f"DVD\t{item.title}\t{item.author}\t"
                    f"{item.year}\t{item.runtime_minutes}\t"
                    f"{item.rating}\t{checked}\n"
                )

            elif item.get_item_type() == "Magazine":

                line = (
                    f"Magazine\t{item.title}\t{item.author}\t"
                    f"{item.year}\t{item.issue_number}\t"
                    f"{item.month}\t{checked}\n"
                )

            file.write(line)


def add_item_interactive(catalog, view):

    try:

        item_type = input("Enter item type (Book/DVD/Magazine): ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        year = int(input("Enter year: "))

        if item_type.lower() == "book":

            isbn = input("Enter ISBN: ")
            page_count = int(input("Enter page count: "))

            item = ItemFactory.create_item(
                item_type,
                title,
                author,
                year,
                isbn,
                page_count
            )

        elif item_type.lower() == "dvd":

            runtime = int(input("Enter runtime minutes: "))
            rating = input("Enter rating: ")

            item = ItemFactory.create_item(
                item_type,
                title,
                author,
                year,
                runtime,
                rating
            )

        elif item_type.lower() == "magazine":

            issue = int(input("Enter issue number: "))
            month = input("Enter month: ")

            item = ItemFactory.create_item(
                item_type,
                title,
                author,
                year,
                issue,
                month
            )

        else:
            raise ValueError("Invalid item type.")

        catalog.add_item(item)

        view.display_message("Item added successfully.")

    except ValueError as e:
        view.display_message(f"Error: {e}")


def main():

    catalog = Catalog()
    view = CatalogView()

    load_catalog(catalog, DATA_FILE)

    view.display_message("Catalog loaded.")

    while True:

        view.display_menu()

        choice = input("Enter choice: ")

        try:

            if choice == "1":

                view.display_items(catalog.get_all_items())

            elif choice == "2":

                keyword = input("Enter title keyword: ")

                results = catalog.search_by_title(keyword)

                view.display_search_results(results, keyword)

            elif choice == "3":

                keyword = input("Enter author keyword: ")

                results = catalog.search_by_author(keyword)

                view.display_search_results(results, keyword)

            elif choice == "4":

                title = input("Enter title to check out: ")

                found = False

                for item in catalog.get_all_items():

                    if item.title.lower() == title.lower():

                        item.check_out()

                        view.display_message("Item checked out.")

                        found = True
                        break

                if not found:
                    view.display_message("Item not found.")

            elif choice == "5":

                title = input("Enter title to check in: ")

                found = False

                for item in catalog.get_all_items():

                    if item.title.lower() == title.lower():

                        item.check_in()

                        view.display_message("Item checked in.")

                        found = True
                        break

                if not found:
                    view.display_message("Item not found.")

            elif choice == "6":

                add_item_interactive(catalog, view)

            elif choice == "7":

                view.display_items(catalog.get_checked_out_items())

            elif choice == "8":

                save_catalog(catalog, DATA_FILE)

                view.display_message("Catalog saved. Goodbye.")

                break

            else:

                view.display_message("Invalid choice.")

        except RuntimeError as e:

            view.display_message(f"Error: {e}")


if __name__ == "__main__":
    main()