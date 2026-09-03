def process_dataset(dataset):
    # Step 1: Parse the strings into useful values
    parsed = map(
        lambda item: (
            item[0],
            float(item[1].split(":")[1].strip()),
            float(item[2].split(":")[1].strip())
        ),
        dataset
    )

    # Step 2: Keep only products costing <= 1000
    filtered = filter(
        lambda item: item[1] <= 1000.0,
        parsed
    )

    # Step 3: Convert each item into a dictionary
    mapped = map(
        lambda item: {
            "product": item[0],
            "price": item[1],
            "score": item[2]
        },
        filtered
    )

    # Step 4: Sort by rating from highest to lowest
    result = sorted(
        mapped,
        key=lambda item: item["score"],
        reverse=True
    )

    return result


data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]

print(process_dataset(data_input))

