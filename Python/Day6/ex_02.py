class CDACStudents():
    course = "PGCP-BDA"

    def __init__(self, name):
        self.name = name

s1 = CDACStudents("Tanishq")
s2 = CDACStudents("Priya")

print(s1.name, "| Course:", s1.course)
print(s2.name, "| Course:", s2.course)
