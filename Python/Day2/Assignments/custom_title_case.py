def main():
    string = input("Enter a string: ")
    '''
    .split() splits a series string literals into substrings and returns a list of substrings
    .capitalize() runs on every word and makes only the first letter capital, 
    .join() joins takes multiple strings and combines them together(uses "" as the separator)
    '''
    string = " ".join([word.capitalize() for word in string.split()])
    print(string)


main()