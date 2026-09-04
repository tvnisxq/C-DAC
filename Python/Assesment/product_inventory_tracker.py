
products = [
{"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10},
{"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50}
]

def menu():
    print("=====USER MENU=====")
    menu_text = '''
    1. Add Product
    2. View All Products
    3. Search Product
    4. Update Product
    5. Delete Product
    6. Exit
    '''
    print(menu_text)
    try:
        choice  = int(input("Enter your choice: "))

    except:
        choice = -1

    return choice

# This adds prodcut in inventories
def add_product():
    try:
        id = int(input("ID: "))
        name = input("Name: ")
        category = input("Category: ")
        price = int(input("Price: "))
        quantity = input("Quantity: ")

    except ValueError:
        print("Please retry with a numerical value")

    print(products) # This gives the default product list
    products.append(dict(id=id, name=name, category=category, price=price, quantity=quantity))
    print(products) # This gives the updated product list(appended)


def view_products():
    print("=====Product Inventory=====")
    # We check if there is any product in the inventory; display if yes 
    if len(products) == 0:
        print("No products found! Add products first")
        return # returns back to the line which called this mf


    # Looping through the product list
    for p in products:

        # Unpacks the current product dictionary and assigns it to variables(note that the order matters here)
        id, name, category, price, quantity = p.values()
        print(f"{id:^5}{name:<20}{category:<20}{price:<10}{quantity:<5}")
    print("="*80)

def search_products():
    try:
        select = int(input("Select the search type: "))

        if select == 1:
            search_by_id() # This calls search_by_id() function

        elif select == 2:
            search_by_name()

        # this handles if user enters invalid numbers.
        else:
            print("Invalid selection! Please retry")

    # this gets executed when user enters string value.
    except:
        print("Please enter an integer input")

# When user enters 1 as selection, search_by_id() gets executed 
def search_by_id():
    id_input = int(input("Enter id to search: "))

    # Using list comprehension to iterate over the product list(each product is a dict here)
    result = [ p for p in products if p["id"]==id_input] 
    # We need to iterate over a specific dict using key: val pair.
    # p["id"] represents the current product's(p) id val
    print(result)
            

# When user enters 2 as selection, search_by_name() gets executed 
def search_by_name():
    name_input = input("Enter name to search: ")

    result = [p for p in products if p["name"]==name_input.title()]
    print(result)



def update_products():
    try:
        select = int(input("Select the product to be updated: "))

        for p in products:
            if select == p['id']:
                new_name = input("New Name: ")

                if new_name: # This is truthy if not empty(False if empty)
                    p['name'] = new_name

 
    except:
        print("Please enter a numerical value")


def delete_products():
    try:
        select = int(input("Enter product id to delete the product: "))

        for p in products:
            if p['id'] == select:
                products.remove(p)
                print("***********")
                print(f"Product {select} deleted!")
                break
            
            else:
                print(f"No Product with id '{select}'")
    except:
        print("Please enter a numerical value as product id")        


def main():

# Imp
    while True:
        choice = menu()
        match choice:
            case 1:
                # Calls add_product function
                add_product()

            case 2:
                # Calls view_product function
                view_products()
            case 3:
                # Calls the search_products function
                search_products()

            case 4:
                # Calls the update_products() function
                update_products()

            case 5:
                # Calls the delete_products() function
                 delete_products()

            case 6:
                break



if __name__ == '__main__':
    main()

