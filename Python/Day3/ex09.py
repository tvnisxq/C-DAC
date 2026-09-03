# Get N and K from the user
N = int(input("Enter number of soldiers (N): "))
K = int(input("Enter elimination interval (K): "))

# Create the soldier circle
soldiers = list(range(1, N + 1))

print("Soldier circle initialized:", soldiers)

# Start counting from index 0
index = 0

# Continue until only one soldier remains
while len(soldiers) > 1:

    # Find the index of the K-th soldier
    index = (index + K - 1) % len(soldiers)

    # Remove that soldier
    eliminated = soldiers.pop(index)

    print(
        f"Eliminated soldier: {eliminated} "
        f"(Remaining: {soldiers})"
    )

# The last remaining soldier is the survivor
print("The sole survivor is:", soldiers[0])