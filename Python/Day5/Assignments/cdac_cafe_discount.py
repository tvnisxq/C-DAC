
def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0):
     # calculate raw subtotal 
     Raw_subtotal = base_price + sum(items)

     # calculates discounted subtotal
     
     discounted_subtotal = Raw_subtotal * (1- discount/100)

     # Calculate Tax

     tax_value = discounted_subtotal * tax_rate

     # Calculate final bill 

     final_bill = tax_value + delivery_fee + discounted_subtotal

     return round (final_bill, 2)

# Example

result = calculate_cafeteria_bill(
    100.0,
    20.0,
    30.0,
    tax_rate=0.08,
    discount=10.0,
    delivery_fee=15.0
)

print(result)