#====================================================================================#
                        # Library Book Management System
#====================================================================================#

#---------------------------Validations----------------------------------------------

# Keep asking the user until they enter some valid value(non-empty string)
def get_text():
    while True:
        value = input("Enter the").strip()

        # returns value when non empty string is entered
        if value != "":
            return value

        else:
            print("Enter a valid value! ")



def get_price():
    while True:
        try:
            price = float(input("Enter the price: "))

            if price > 0.0:
                return price

            else:
                print("price must be greater then 0 or positive number.")

        except ValueError:
            print("Invalid value! please retry!")

def get_copies():
    while True:
        try:
            copies = int(input("Enter the no. of copies : " ))
            if copies >= 0:
                return copies

            else:
                print("copies must be an integer")

        except ValueError:
            print("Entry must be an integer")



def get_id():
    while True:
        try:
            book_id = int(input("Enter the id: "))
            return book_id
        except ValueError:
            print("Enter number only.")




#==========================================================================#
def menu():
    while True:

        print("1. Add Book\n")
        print("2. View Catalog\n")
        print("3. Search Books\n")
        print("4. Update Details\n")
        print("5. Delete File\n")
        print("6. Save File\n")
        print("7. Load from File\n")
        print("8. Exit \n")

        try:
            choice = int(input("Enter your choice : "))

            if 1 <= choice <= 8:
                return choice
            else:
                print("Please enter from the available choices!")

        except:
            print("Invalid Choice! Please try again")


#=============================ADD BOOK======================================#
def add_book_entry(catalog: list[dict], next_id: int) -> int:
    book = {

        "id" : next_id,
        "title" : get_text(),
        "author" : get_text(),
        "genre" : get_text(),
        "price"  : get_price(),
        "copies"  :get_copies()

    }
    catalog.append(book)
    print("Book added successfully!!!")
    return next_id + 1


#================================VIEW CATALOG======================================#
def render_catalog(catalog: list[dict]) -> None:
    # if len(catalog) == 0:
    if not catalog:
        print("No books found. Please add first")

    elif len(catalog) == 1:
        print(catalog[0])

    else:
        
        print("==========CATALOG=========")
        for c in catalog:
            print(f"ID:               {id}")
            print(f"Title:            {'title'}")
            print(f"Author:           {'author'}")
            print(f"Genre:            {'genre'}")
            print(f"Price:            {'price'}")
            print(f"Copies:           {'copies'}")

        print("==========================")

        return c

          
def main():
    next_id = 1
    catalog = []

    while True:

        choice = menu()
        match choice:

            case 1:
                add_book_entry(catalog, next_id=1)
            case 2:
                render_catalog()
            case 3:
                exit


if __name__ == "__main__":
    main()