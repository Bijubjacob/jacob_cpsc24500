# Week 8 Final Project Template

Starter files for the Library Catalog System.

## Build order
1. `library_item.py` - the abstract base class
2. `book.py` - one concrete subclass, test it
3. `catalog.py` - the singleton catalog
4. `catalog_view.py` - the view
5. `main.py` - wire it all together with one item type
6. `dvd.py` and `magazine.py` - add the other types
7. `item_factory.py` - the factory pattern
8. File loading/saving in `main.py`

Commit after each step.

## Files
- `library_item.py`, `book.py`, `dvd.py`, `magazine.py` - model classes
- `catalog.py` - singleton catalog
- `item_factory.py` - factory for creating items by type string
- `catalog_view.py` - view (display only, no data storage)
- `main.py` - controller and entry point
- `data/catalog.tsv` - sample data file
