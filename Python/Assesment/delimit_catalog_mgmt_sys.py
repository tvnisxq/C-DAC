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

    print("."*60)

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
    return next_id + 1

#=========================================================================

def render_catalog(catalog: list[dict]) -> None:
    """Displays formatted tabular catalog or single-record card when count == 1."""

    # Checking if the catalog is empty
    if not catalog:
        print("Catalog is empty. Please add a book first")
        return 

    # If there is excatly 1 book in the catalog, show single card entry
    if len(catalog) == 1:
        book = catalog[0]

        print("\n========Book Details========")
        for key, val in book.items():
            print(f"{key.title()}: {val}")

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
def query_books(catalog: list[dict]) -> list[dict]:
    """Returns filtered list matching ID or case-insensitive title/author substring."""
       
    print("=================SEARCH BOOKS=====================")
    search_term = input("Enter the Search Term: ").strip()

    # If the search_temr is int: use id to search
    if search_term.isdigit():
        search_id = int(search_term)
        results = [book for book in catalog if search_id==book['id']]
        return results

    # Otherwise search using the name
    else:
        search_name = search_term.lower()
        results = [book for book in catalog if search_name in book['title'].lower() or search_name in book['author'].lower()]
        return results


#=========================================================================
def modify_book_details(catalog: list[dict], book_id: int) -> bool:
    """Updates price and copies for the specified book ID; returns success status."""
    try:

        for book in catalog:
            if int(book_id) == book['id']:
                new_price = float(input("New Price: "))
                new_copies = int(input("New Copies: "))

                book['price'] = new_price
                book['copies'] = new_copies

                print("Book details updated successfully!!!")

                return True
        else:
            print(f"No book found for ID: {book_id} !!!")
            return False


    except ValueError: # Avoiding bare except
        print("Please enter a numerical value !!!")

#=========================================================================
def delete_books():
    ...

#=========================================================================

def sync_catalog_to_file(filepath: str, catalog: list[dict]) -> None:
    """Serializes each book dictionary into pipe-delimited strings in write mode."""
    with open('books.txt', 'w') as file:
        for b in catalog:
            id, title, author,genre, price, copies  = b.values()
            books_file = file.write(f"{id}|{title}|{author}|{genre}|{price}|{copies}\n")
    print("Catalog saved Successfully!")

#=========================================================================

def load_catalog_from_file(filepath: str) -> list[dict]:
    """Parses books.txt line-by-line using split('|') and reconstructs dictionary list."""
    catalog  = []

    with open('books.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('|')

            id, title, author, genre, price, copies = parts

            # Everything read from a file is a string.
            # So we convert numeric values back to their original types.
            book = {
                'id': int(id),
                'title': title,
                'author': author,
                'genre': genre,
                'price': float(price),
                'copies': int(copies)
            }

            # Add the reconstructed dictionary back to catalog
            catalog.append(book)

    return catalog


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
                next_id = add_book_entry(catalog, next_id)         

            case 2:
                render_catalog(catalog)

            case 3:
                if not catalog:
                    print("Catalog Empty! Please add first")

                else:
                    results = query_books(catalog)
                    
                    if results:     # Print results if not empty
                        render_catalog(results)
                    
                    else:       # Else print message 
                        print("No matching books found !!!")
                    
            case 4:
                book_id = int(input("Enter ID to update: "))
                success = modify_book_details(catalog, book_id)


            case 5:
                ...

            case 6:
                if not catalog:
                    print("Empty Catalog! Please add first")
                else:
                    sync_catalog_to_file('books.txt', catalog)

            case 7:
                filepath = 'books.txt'
                catalog = load_catalog_from_file(filepath)
                print("Catalog loaded Successfully!")

            case 8:
                break


if __name__ == '__main__':
    main()