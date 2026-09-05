products = [{"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10},
{"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50}]


next_id = len(products) + 1 if products else 0

def menu():
    menu_txt = '''
    1. Add Product
    2. View All Products
    3. Search Product
    4. Update Product
    5. Delete Product
    6. Exit
'''
    print(menu_txt)
    choice = int(input("Enter your choice: "))
    try:
        if choice != int(choice):
            print("Enter an integer value: ")

    except ValueError:
        print("Invalid Entry! Retry")

    return choice


#+================================#
       # validations
#=================================#
def get_product_id():
    while True:
        try: 
            id = int(input("Enter the id: "))
            break
        except ValueError:
            print("Please enter a valid integer")
    return id       

def get_product_name():
    while True:
        name = input("Enter the name: ").strip()
        if name != "":
            break
        print("Name can't be empty! please retry.")
    return name

#================================#
def get_product_category():
    while True:
        category =input("Enter the category: ").strip()
        if category == "": 
            print("category can't be empty")

        elif category.isdigit():
            print("category can't be in integer") 

        else:
            return category

#===============================#
def  get_product_price():
    while True:
        try:
            price =float(input("Enter the price: "))

            if price > 0:
                break
            print("price must be greater than 0. positive value.")

        except ValueError:
            print("Invalid value please retry..")

    return price
#================================#
def get_product_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))

            if quantity >= 0 :
                break
            print("quantity must be greater than or equal to 0")
        except ValueError:
            print("Invalid value please retry..")

    return quantity
#================================#

def add_products():
    try:
        id = get_product_id()
        name = get_product_name()
        category = get_product_category()
        price = get_product_price()
        quantity = get_product_quantity()

        # print(products)
        products.append(dict(id=id, name=name, category=category, price=price, quantity=quantity))
        print(products)    
        
    except ValueError:
        print("Invalid value please retry!")
        

#===============================#
def view_products():
    if len(products) == 0:
        print("Empty list! please add first. ")
        return 

    # Unpacking
    for p in products:
        id, name, category, price, quantity =  p.values()

        if products[len(products)//2]:
            print("="*50)
        print(f"ID      :                            {id}")
        print(f"Name    :                            {name}")
        print(f"Category:                            {category}")
        print(f"Price   :                            {price}")
        print(f"Quantity:                            {quantity  }")



#==============================#

def search_products():
    # search using product_id

    try:
        select = int(input("Enter search type: "))
        if select == 1:
            search_by_id()

        elif select == 2:
            search_by_name()

    except ValueError:
        print("Invalid selection! please retry. ")



def search_by_id():
    input_id = int(input("Enter the id: "))
    result = [p for p in products if p["id"] == input_id]
    print(result)

def search_by_name():
    input_name =input("Enter the name: ")
    result = [p for p in products if p["name"] == input_name.title()]
    if result == []:
        print("No results found! Please add first")
    else:
        print(result)
#==============================#

def update_products():
    pass
#==============================#


def delete_products():
    pass

#==============================#


def main():

    # Choice must be stored in a variable after the return brings the input back to main()
    while True:

        choice = menu()   # 1
        if choice == 1:
            add_products()

        elif choice == 2:
            view_products()

        elif choice ==3 :
            search_products()

        # elif choice == 4:
        #     update_products()

        # elif choice == 5 :
        #     delete_products()

        else:
            break


if __name__ == "__main__":

    main()