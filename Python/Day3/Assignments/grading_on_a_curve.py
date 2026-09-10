# Get scores from the user and convert them to integers
scores = list(map(int, input("Enter scores: ").split()))

# Apply the curve using one list comprehension
curved = [
    min(100, score + 10 if score < 50 else score + 5)
    for score in scores
]

# Print original and curved grades
print("Original:", scores)
print("Curved:", curved)