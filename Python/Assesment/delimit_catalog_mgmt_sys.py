from typing import List, Dict
def menu():
    menu_text = '''
    1. Add Book Entry
    2. View Catalog
    3. Search Books
    4. Update details
    5. Delete Book
    6. Save to file
    7. Load from file
    8. Exit
'''
    print(menu_text)
    print("."*50)
    print("=======CATALOG MANAGEMENT SYSTEM=======")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError: 
        choice = -1

    print("."*50)

    return choice

#===================================================================================
def add_book_entry(catalog: List[Dict], next_id: int) -> int:
    """Prompts user for book details, appends new dict, returns updated ID counter."""


    # Title input & Validation
    while True:
        title = input("Title: ").strip()
        '''
        After strip, an empty string means the user entered nothing
        or only whitespace
        '''
        if title != "":
            break
        print("Title cannot be empty! ")


    # Author input and Validation
    while True:
        author = input("Author: ").strip()

        if author != "":
            break
        print("'Author' only accepts strings!")


    # Genre input and Validation
    while True:
        genre = input("Genre: ").strip()

        if genre != "":
            break
        print("'Genre only accepts strings!'")


    # Price input and Validation
    while True:
        try: 
            price = float(input("Price: "))

            if price > 0:
                break
            print("'Price' only accepts Positive integers!")


        # This happens if float cannot convert the input
        # Example: 'Hello'
        except ValueError:
            print("Please enter a valid value for price ")


    # Copies input and validation
    while True:
        try:
            copies = int(input("Copies: "))

            # Copies can be 0, but not negative
            if copies >= 0:
                break
            print("Copies cannot be negative!")


        # Handles inputs like 0 or 5.5
        except ValueError:
           print("Invalid value(s) have been supplied to field(s)")

    catalog.append(dict(id=next_id, title=title, author=author, genre=genre, price=price, copies=copies))

#=========================================================================

def render_catalog(catalog: list[dict]) -> None:
    """Displays formatted tabular catalog or single-record card when count == 1."""

    # Checking if the catalog is empty
    if not catalog:
        print("Catalog is empty. Please add a book first")
        return 

    # If there is only 1 book in the catalog, show single card entry
    if len(catalog) == 1:
        book = catalog[0]

        print("\n========Book Details========")
        for key, val in book.items():
            print(f"{key}: {val}")

        print("==============================")
        return 

    # Display multiple books in a formatted table
    print("\n" + "="*85)

    # Print Column headers
    print(
        f"{'ID': <5}"
        f"{'Title': <25}"
        f"{'Author': <25}"
        f"{'Genre': <15}"
        f"{'Price': <10}"
        f"{'Copies': <8}"
    )
    print("."*80)

    # print each book
    for book in catalog:
        print(
            f"{book['id']:<5}"
            f"{book['title']:<25}"
            f"{book['author']:<25}"
            f"{book['genre']:<15}"
            f"{book['price']:<10.2f}"
            f"{book['copies']:<8}"
        )
    print("="*80)




#=========================================================================
def main():

    catalog = []
    next_id = 1

    while True:

        # Calls the menu function and choice val gets assigned to choice
        choice = menu()
        match choice:
            case 1:
                # Calls the add_book_entry function 
                add_book_entry(catalog, next_id=1)         

            case 2:
                render_catalog(catalog)


if __name__ == '__main__':
    main()
