vip_queue = ["Guido", "Esha", "Rajan", "Kishori"]

while True:
    print("Current VIP queue:", vip_queue)

    guest = input("Enter guest name: ")

    # Stop the program if the user types exit
    if guest == "exit":
        break

    # Check whether the guest is on the VIP list
    if guest in vip_queue:
        # Find the guest's current position
        index = vip_queue.index(guest)

        # Remove the guest from the current position
        vip_queue.pop(index)

        # Insert the guest at the front
        vip_queue.insert(0, guest)

        print(guest, "moved to the front!")
    else:
        print("Access denied. Not on the VIP list.")

    print()