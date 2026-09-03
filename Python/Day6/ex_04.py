class MathUtility:
    @staticmethod
    def is_even(num):   
        return num%2 == 0

print(MathUtility.is_even(10))
n1 = MathUtility.is_even(10)

# Bad Practice
print(n1.is_even) # This one shows Attribute error