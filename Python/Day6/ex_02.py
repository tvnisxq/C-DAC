# Instance Variables: Defined inside methods (usually __init__) prefixed with self.. They belong to a specific object instance.
# Class Variables: Defined directly inside the class body but outside any methods. They are shared across all instances of the class.

class CDACStudents():
    course = "PGCP-BDA"

    def __init__(self, name):
        self.name = name

s1 = CDACStudents("Tanishq")
s2 = CDACStudents("Priya")

print(s1.name, "| Course:", s1.course)
print(s2.name, "| Course:", s2.course)
