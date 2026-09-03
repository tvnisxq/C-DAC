import re

class Patient:
    # Class variable to track total patient instances created
    _patient_counter = 0

    @staticmethod
    def validate_dob_format(dob_str: str) -> bool:
        """
        Validates if the date of birth string matches the exact 'YYYY-MM-DD' format 
        using regular expressions.
        """
        # Regex: 4 digits, hyphen, 2 digits, hyphen, 2 digits
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        return bool(re.match(pattern, dob_str))

    def __init__(self, name: str, dob: str):
        # Check if the date of birth is valid. raise ValueError if it fails
        if not Patient.validate_dob_format(dob):
            raise ValueError(f"Invalid date of birth format: '{dob}'. Expected YYYY-MM-DD.")
        
        # Increment the patient counter on successful validation
        Patient._patient_counter += 1
        
        # Assign a unique sequential patient ID (e.g., PAT-1001)
        self.patient_id = f"PAT-{1000 + Patient._patient_counter}"
        
        # Set instance attributes
        self.name = name
        self.dob = dob

    @classmethod
    def get_total_patients(cls) -> int:
        """
        Class method to return the current value of the patient counter.
        """
        return cls._patient_counter

# 1. Valid Registration
p1 = Patient("Arham Khan", "1999-05-15")
print(p1.patient_id)  # Output: PAT-1001

# 2. Invalid DOB registration (throws ValueError)
try:
    p2 = Patient("Lisa", "12/08/1998")
except ValueError as e:
    print(e)  # Output: Invalid date of birth format: '12/08/1998'. Expected YYYY-MM-DD.

print(Patient.get_total_patients())  # Output: 1