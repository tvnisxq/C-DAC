def manage_bookstore_inventory(inventory, action, book_title, quantity=0):

    if action == "add":

        # If the book exists, add to its current quantity.
        # If it doesn't, get() returns 0, so it becomes a new book.
        inventory[book_title] = inventory.get(book_title, 0) + quantity

    elif action == "sell":

        # First verify that the book exists.
        if book_title not in inventory:
            print(f"Error: Book '{book_title}' not found in inventory.")

        # Then check whether enough copies are available.
        elif quantity > inventory[book_title]:
            print(
                f"Error: Insufficient stock for '{book_title}'. "
                f"Available: {inventory[book_title]}."
            )

        else:

            # Sale is valid, so subtract the quantity.
            inventory[book_title] -= quantity

            # Remove the book completely when its stock becomes zero.
            if inventory[book_title] == 0:
                del inventory[book_title]

    elif action == "lookup":
        # get(..., 0) safely returns 0 if the book is absent.

        # print(inventory.get(book_title, 0))
        # print(f"Stock of '{book_title}': {inventory.get(book_title, 0)}")
        return inventory.get(book_title, 0)

    else:
        print("Error: Invalid action.")

    return inventory


# Initial Inventory
inventory = {"Python Basics": 10, "Learning AI": 5}

# 1. Add Stock
inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)

# 2. Sell Stock Safely (Missing Book)
inventory = manage_bookstore_inventory(inventory, "sell", "Data Science 101", 1)

# 3. Sell Stock (Insufficient)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)

# 4. Sell Stock (Exactly Zero Stock)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)

print(inventory)

print(
        manage_bookstore_inventory(
        inventory, "lookup", "Python Basics"
    )
)
