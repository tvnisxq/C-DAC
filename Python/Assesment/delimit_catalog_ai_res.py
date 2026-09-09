from typing import List, Dict


# =============================================================================
def menu():

    menu_text = """
    1. Add Book Entry
    2. View Catalog
    3. Search Books
    4. Update details
    5. Delete Book
    6. Save to file
    7. Load from file
    8. Exit
"""

    print(menu_text)
    print("." * 50)
    print("=======CATALOG MANAGEMENT SYSTEM=======")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        # Returning -1 ensures the program doesn't crash
        # when the user enters something other than a number.
        choice = -1

    print("." * 60)

    return choice


# =============================================================================
def add_book_entry(catalog: List[Dict], next_id: int) -> int:
    """
    Prompts user for book details,
    appends a new dictionary to catalog,
    and returns the next available ID.
    """

    # ---------------- TITLE VALIDATION ----------------
    while True:
        title = input("Title: ").strip()

        if title:
            break

        print("Title cannot be empty!")


    # ---------------- AUTHOR VALIDATION ----------------
    while True:
        author = input("Author: ").strip()

        if author:
            break

        print("Author cannot be empty!")


    # ---------------- GENRE VALIDATION ----------------
    while True:
        genre = input("Genre: ").strip()

        if genre:
            break

        print("Genre cannot be empty!")


    # ---------------- PRICE VALIDATION ----------------
    while True:

        try:
            price = float(input("Price: "))

            # Price must be positive.
            if price > 0:
                break

            print("Price must be greater than 0!")

        except ValueError:
            print("Please enter a valid numerical value for price!")


    # ---------------- COPIES VALIDATION ----------------
    while True:

        try:
            copies = int(input("Copies: "))

            # Copies can be 0, but cannot be negative.
            if copies >= 0:
                break

            print("Copies cannot be negative!")

        except ValueError:
            print("Please enter a valid integer value for copies!")


    # Add the new book dictionary to catalog.
    catalog.append(
        {
            "id": next_id,
            "title": title,
            "author": author,
            "genre": genre,
            "price": price,
            "copies": copies
        }
    )

    # Return the next ID for future books.
    return next_id + 1


# =============================================================================
def render_catalog(catalog: list[dict]) -> None:
    """
    Displays formatted tabular catalog.
    Displays a detailed card when there is exactly one book.
    """

    # Check whether catalog is empty.
    if not catalog:
        print("Catalog is empty. Please add a book first.")
        return


    # If only one book exists, display detailed information.
    if len(catalog) == 1:

        book = catalog[0]

        print("\n======== Book Details ========")

        for key, value in book.items():
            print(f"{key.title()}: {value}")

        print("==============================")

        return


    # ---------------- MULTIPLE BOOKS TABLE ----------------
    print("\n" + "=" * 85)

    print(
        f"{'ID':<5}"
        f"{'Title':<25}"
        f"{'Author':<25}"
        f"{'Genre':<15}"
        f"{'Price':<10}"
        f"{'Copies':<8}"
    )

    print("." * 80)


    # Print every book in the catalog.
    for book in catalog:

        print(
            f"{book['id']:<5}"
            f"{book['title']:<25}"
            f"{book['author']:<25}"
            f"{book['genre']:<15}"
            f"{book['price']:<10.2f}"
            f"{book['copies']:<8}"
        )

    print("=" * 85)


# =============================================================================
def query_books(catalog: list[dict]) -> list[dict]:
    """
    Returns books matching:

    - Exact ID
    - Case-insensitive substring in title
    - Case-insensitive substring in author
    """

    print("================= SEARCH BOOKS =================")

    search_term = input("Enter the Search Term: ").strip()


    # ---------------- SEARCH BY ID ----------------
    if search_term.isdigit():

        search_id = int(search_term)

        results = [
            book
            for book in catalog
            if search_id == book["id"]
        ]

        return results


    # ---------------- SEARCH BY TITLE / AUTHOR ----------------
    search_name = search_term.lower()

    results = [
        book
        for book in catalog
        if (
            search_name in book["title"].lower()
            or search_name in book["author"].lower()
        )
    ]

    return results


# =============================================================================
def modify_book_details(catalog: list[dict], book_id: int) -> bool:
    """
    Updates price and copies for a specific book ID.

    Returns:
        True  -> Update successful
        False -> Update failed
    """

    # Find the requested book.
    for book in catalog:

        if book["id"] == book_id:

            # ---------------- NEW PRICE VALIDATION ----------------
            while True:

                try:
                    new_price = float(input("New Price: "))

                    if new_price > 0:
                        break

                    print("Price must be greater than 0!")

                except ValueError:
                    print("Please enter a valid numerical value!")


            # ---------------- NEW COPIES VALIDATION ----------------
            while True:

                try:
                    new_copies = int(input("New Copies: "))

                    if new_copies >= 0:
                        break

                    print("Copies cannot be negative!")

                except ValueError:
                    print("Please enter a valid integer value!")


            # Update the dictionary directly.
            book["price"] = new_price
            book["copies"] = new_copies

            print("Book details updated successfully!")

            return True


    # This executes if no matching ID was found.
    print(f"No book found for ID: {book_id}")

    return False


# =============================================================================
def delete_books(catalog: list[dict], book_id: int) -> bool:
    """
    Deletes a book after user confirmation.

    Returns:
        True  -> Book deleted
        False -> Book not deleted
    """

    # enumerate() gives us both:
    # index -> position in list
    # book  -> actual dictionary
    for index, book in enumerate(catalog):

        if book["id"] == book_id:

            select = input(
                "Are you sure you want to delete this book [y/n]: "
            ).strip().lower()


            if select == "y":

                # Delete the book using its list index.
                del catalog[index]

                print("Book removed successfully!")

                return True


            else:
                print("Book deletion cancelled.")

                return False


    # Executes if no book matches the given ID.
    print(f"No book found for ID: {book_id}")

    return False


# =============================================================================
def sync_catalog_to_file(filepath: str, catalog: list[dict]) -> None:
    """
    Serializes each book dictionary into pipe-delimited strings.

    Example:
    1|Python Programming|John Zelle|Technical|650.0|15
    """

    # IMPORTANT:
    # Use filepath instead of hardcoding 'books.txt'.
    with open(filepath, "w") as file:

        for book in catalog:

            # Explicit dictionary access is clearer than using .values().
            #
            # It also makes the file format independent of dictionary
            # insertion order.
            file.write(
                f"{book['id']}|"
                f"{book['title']}|"
                f"{book['author']}|"
                f"{book['genre']}|"
                f"{book['price']}|"
                f"{book['copies']}\n"
            )

    print("Catalog saved successfully!")


# =============================================================================
def load_catalog_from_file(filepath: str) -> list[dict]:
    """
    Reads the pipe-delimited file and reconstructs
    the catalog as a list of dictionaries.
    """

    # Create an empty catalog before reading the file.
    catalog = []


    try:

        # IMPORTANT:
        # Reading mode is 'r', not 'w'.
        #
        # 'w' would erase the existing file contents.
        with open(filepath, "r") as file:

            lines = file.readlines()


            # Process each line/book separately.
            for line in lines:

                # Remove newline and split using pipe delimiter.
                parts = line.strip().split("|")


                # Skip empty lines.
                if not parts or parts == [""]:
                    continue


                # Each valid record should contain 6 values.
                if len(parts) != 6:
                    print(f"Skipping invalid record: {line.strip()}")
                    continue


                # Unpack the six values.
                book_id, title, author, genre, price, copies = parts


                # Everything read from a file is initially a string.
                # Convert numeric values back to their correct types.
                book = {
                    "id": int(book_id),
                    "title": title,
                    "author": author,
                    "genre": genre,
                    "price": float(price),
                    "copies": int(copies)
                }


                # Add reconstructed dictionary to catalog.
                catalog.append(book)


    except FileNotFoundError:

        # First-time users may not have a books.txt file yet.
        print("No saved catalog file found.")

        return []


    except ValueError:

        # Handles corrupted numeric data in the file.
        print("Invalid data found in the catalog file.")

        return []


    return catalog


# =============================================================================
def main():

    # The catalog starts empty when the program starts.
    catalog = []

    # First book gets ID 1.
    next_id = 1

    # File location used by save/load operations.
    filepath = "books.txt"


    while True:

        choice = menu()


        match choice:

            # =============================================================
            # ADD BOOK
            case 1:

                next_id = add_book_entry(catalog, next_id)


            # =============================================================
            # VIEW CATALOG
            case 2:

                render_catalog(catalog)


            # =============================================================
            # SEARCH BOOKS
            case 3:

                if not catalog:
                    print("Catalog Empty! Please add a book first.")

                else:

                    results = query_books(catalog)

                    if results:
                        render_catalog(results)

                    else:
                        print("No matching books found!")


            # =============================================================
            # UPDATE BOOK
            case 4:

                try:

                    book_id = int(
                        input("Enter ID to update: ")
                    )

                    modify_book_details(catalog, book_id)


                except ValueError:

                    # Prevents invalid input from crashing the program.
                    print("Please enter a valid numerical ID!")


            # =============================================================
            # DELETE BOOK
            case 5:

                try:

                    book_id = int(
                        input("Enter ID to delete: ")
                    )

                    delete_books(catalog, book_id)


                except ValueError:

                    print("Please enter a valid numerical ID!")


            # =============================================================
            # SAVE TO FILE
            case 6:

                if not catalog:

                    print("Empty Catalog! Please add a book first.")

                else:

                    sync_catalog_to_file(filepath, catalog)


            # =============================================================
            # LOAD FROM FILE
            case 7:

                catalog = load_catalog_from_file(filepath)


                if catalog:

                    # IMPORTANT:
                    # After loading existing books, calculate the next ID.
                    #
                    # Example:
                    # Existing IDs: 1, 2, 3
                    # Next ID should be: 4
                    next_id = max(
                        book["id"] for book in catalog
                    ) + 1

                    print("Catalog loaded successfully!")

                else:

                    print("No books were loaded.")


            # =============================================================
            # EXIT
            case 8:

                print("Exiting Catalog Management System...")

                break


            # =============================================================
            # INVALID MENU OPTION
            case _:

                print("Invalid choice! Please select an option from 1 to 8.")


# =============================================================================
if __name__ == "__main__":
    main()