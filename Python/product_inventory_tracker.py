products = [
{"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10},
{"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50}
]

def menu(): 

    menu_text = '''

    ====== USER MENU ======
    1. Add Product
    2. View All Products
    3. Search Product
    4. Update Product
    5. Delete Product
    6. Exit
    =======================
''' 
    print("Product Inventory Management System")
    print(menu_text)

    try:
        choice = int(input("Enter your choice: "))
    except:
        choice = -1


def add_product():
    try:
        global id_counter

        print("==========Add New Product==========")
        name = input("Name :")
        category = input("Name :")
        price = input("Price :")
        Quantity = input("Quantity :")

        # Generate the new id
        pid = id_counter + 1

    except 

def view_products():
    pass

def search_products():
    pass

def update_product():
    pass

def delete_product():
    pass




def main():
    '''
    1. Add Product
    2. View All Products
    3. Search Product
    4. Update Product
    5. Delete Product
    6. Exit
    '''
    while True:
        # The entered choice is calling the user menu
        choice = menu()

        # Conditionals for triggering a specific function according to entered choice
        match choice:

            case 1:
                add_product()

            case 1:
                pass

            case 1:
                pass

            case 1:
                pass

            case 1:
                pass

            case 1:
                pass

            case 1:
                pass

        