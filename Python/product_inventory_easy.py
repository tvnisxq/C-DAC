products = [{"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10},
{"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50}]

next_id = len(products) + 1 if products else 0
print(next_id)

#+================================#
       # validations
#=================================#
def get_prroduct_name():
    while True:
        name = input("Enter the name: ").strip()
        if name != "":
            break
        print("Name can't be empty! please retry.")

#================================#
def get_product_category():
    while True:
        category =input("Enter the category: ").strip()
        if category != "":
            return category
        print("Category can't be empty: ")

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


def main():
    pass

#================================#
def add_products():

    name = input("Enter the name: ")
    category =input("Enter the category: ")
    price =float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    products.append()
    













    if __name__ == "__main__":

        main()

