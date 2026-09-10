# Create a 5 x 5 grid filled with dots
grid = [["." for col in range(5)] for row in range(5)]

# Place food at row 2, column 3
grid[2][3] = "F"

# Get snake's position from the user
row = int(input("Enter row: "))
col = int(input("Enter column: "))

# Place the snake's head
grid[row][col] = "S"

# Check if the snake ate the food
if row == 2 and col == 3:
    print("Yum! The snake ate the food!")

# Print the grid
for row in grid:
    print(" ".join(row))