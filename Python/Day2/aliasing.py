# Aliasing(Sharing referencews)
#! Aliasing is generally avoided

list1 = [10, 20, 30]
list2 = list1

list2.append(99)
print(list1)
print(id(list1) == id(list2))