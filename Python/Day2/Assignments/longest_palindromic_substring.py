def longestPalindrome():
    text = input("Enter a text: ")

    # Initializing the longest to be empty string
    longest = ""
    len_text = len(text)

    '''
    Using Nested for loops here:
    1. The outer loop keeps iterating over the string till the end
    2. The inner loop keeps iterating over it too but from the index one greter
       than the start index(of the outer loop) and one greater as well(cuz last index is exclusive)
    '''
    for i in range(len_text):
        for j in range(i + 1, len(text) + 1):
            # Extracting the substring(start_index:i, end_index:)
            # Example: text[0:1] = b, text[0:3] = bab
            sub_str = text[i:j]         

            # Then we check if the sub_str is a palindrom(same after reversing or not)
            if sub_str == sub_str[::-1]:
                # If the substring length is longer than the longest(init to 0)
                if len(sub_str) > len(longest):
                    longest = sub_str # we update the longest to be that substring
    print(longest)

longestPalindrome()