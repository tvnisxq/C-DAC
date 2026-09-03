cargo = ["coal", "iron", "gold", "coal", "timber", "coal"]

resource = input("Enter resource: ")

if resource in cargo:
    count = cargo.count(resource)
    first_index = cargo.index(resource)

    print(f"Number of {resource} wagons: {count}")
    print(f"First {resource} wagon is at index: {first_index}")
else:
    print("Resource not found on train!")