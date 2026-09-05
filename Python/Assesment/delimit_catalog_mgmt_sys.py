from typing import list, Dict
def menu():
    menu_text = '''
    1. Add Book Entry
    2. Display Catalog
    3. Search Books
    4. Update details
    5. Sync Catalog to file
    6. Load Catalog from file
'''
    print("."*50)
    print("=======CATALOG MANAGEMENT SYSTEM=======")

    try:
        choice = int(input("Enter your choice: "))
    except:
        choice = -1

    print("."*50)

    return choice

    


def add_book_entry(list[Dict], next_id: int) -> int:
"""Prompts user for book details, appends new dict, returns updated ID counter."""


def main():
    while True:

        # Calls the menu function and choice val gets assigned to choice
        choice = menu()
        match choice:
            case 1:
                # Calls the add_book_entry function 
                add_book_entry()         

            case 2:
                ...


if __name__ == '__main__':
    main()
