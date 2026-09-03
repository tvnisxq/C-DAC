coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]

valid_coords = [
    coordinate
    for coordinate in coords
    if coordinate[0] > 0 and coordinate[1] > 0
]

print(valid_coords)



