items = ["staff", "potion", "spellbook"]

print("Portal transition activated!")

# Get the new item from the user
new_item = input("Enter new item: ")

# Add the new item to the end
items.append(new_item)

# Remove the oldest item (index 0)
ejected = items.pop(0)

# Print the results
print("Ejected oldest item:", ejected)
print("Current items in the magic bag:", items)