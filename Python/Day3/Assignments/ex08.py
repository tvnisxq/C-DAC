cart = ["apple", "banana", "apple", "orange", "banana", "banana"]

seen = set()
cleaned_cart = []

for item in cart:
    if item not in seen:
        cleaned_cart.append(item)
        seen.add(item)

print(cleaned_cart)