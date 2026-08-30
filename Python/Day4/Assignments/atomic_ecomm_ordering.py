from typing import Dict

class OutOfStockError(Exception):
    pass
class ProductNotFoundError(Exception):
    pass


def main():
    catalog = {
        "P01": {"price": 10.0, "stock": 5},
        "P02": {"price": 20.0, "stock": 10}
    }
    
    total = process_order(catalog, {"P01": 2, "P02": 1})
    print(f"The total is: {total}")

    print(f"Catalog after the successful order: {catalog}")


    try:
        total = process_order(catalog, {"P01": 2, "P02": 15})
    except OutOfStockError as e:
        print(e)
    print(f"Catalog after failed order: {catalog}")


    try:
        new_order = process_order(catalog, {"P01": 2, "P99": 3})
    except ProductNotFoundError as e:
        print(e)
    print(f"Catalog after failed order: {catalog}")



def process_order(catalog: Dict[str, Dict], order: Dict[str, int]) -> float:
    for product_id, quantity in order.items():
        if product_id not in catalog:
            raise ProductNotFoundError(f"Product '{product_id}' not found in store catalog.")

        if quantity > catalog[product_id]["stock"]:
            raise OutOfStockError(f"Product '{product_id}' is out of stock. Requested: {quantity}, Available: {catalog[product_id]["stock"]}") 


    total = 0.0
    for product_id, quantity in order.items():
        total += catalog[product_id]["price"] * quantity


    for product_id, quantity in order.items():
        catalog[product_id]["stock"] -= quantity

    return total


if __name__ == "__main__":
    main()