class DateConverter:
    def __init__(self, year, month, day):

        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_string(cls, date_str):    
        parts = list(map(int, date_str.split("-")))
        return cls(parts[0], parts[1], parts[2])

date_obj = DateConverter.from_string("2026-08-28")
print(date_obj.year)
print(date_obj.month)
print(date_obj.day)
