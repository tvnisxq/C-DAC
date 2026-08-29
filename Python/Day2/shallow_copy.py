# Shallow copy with simple values
simple1 = [1, 2, 3]
simple2 = simple1.copy()
simple2.append(99)
print(simple1) #[1, 2, 3] Original is unaffected

# Shallow copy with inner lists(shares reference to innner lists)
nested1 = [[1, 2], [3, 4]]
nested2 = nested1.copy()

# Modifying the nested sublist in the copy
nested2[0][0] = 99
print(nested1) # Original was modified!
print(id(nested1[0]) == id(nested2[0])) 
