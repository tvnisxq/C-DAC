class Student:
    # Constructor/Initializer method
    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age # Instance attribute

    # Instance method
    def display_details(self):
        return f"Student: {self.name}, Age: {self.age}"

# Instantiation
student_1 = Student("Arham", 21)
print(student_1.display_details()) # Output: Student: Arham, Age: 21
