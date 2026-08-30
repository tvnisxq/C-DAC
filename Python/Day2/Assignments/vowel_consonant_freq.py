from collections import defaultdict
def main():
    string = input("Enter a string: ")
    '''
    Hard coded vowels for tracking if the current character 
    is one of the characters that also exists in 'vowels'
    '''
    vowels = "aeiouAEIOU"

    '''
    Initializing a defaultdict with integer 0 by default.
    If the keys are not there, It wont return a key error 
    and if keys are there, it willl just increment them
    '''
    vowel_count = defaultdict(int)
    consonant_count = 0

    # Problem asks to handle it case-insensitively
    for char in string.lower():
        # This check will process only alphabets
        if char.isalpha():
            # Check if the character is in vowels:
            if char in vowels:
                vowel_count[char] += 1
            else:
                consonant_count += 1

    print("Vowel Frequencies: ") 
    for vow, freq in vowel_count.items():
        print(f"{vow}: {freq}")

    print(f"Total Consonants: {consonant_count}")
    
main()