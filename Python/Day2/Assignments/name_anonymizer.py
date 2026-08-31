def main():
    name = input("Enter a name: ")

    list_name = name.split()

    # We loop through the range len(list) - 1 so as to exclude the last name
    for i in range(len(list_name)-1):
        '''
        Then here we replace the lower case letters in the name with "."
        And keep the first letter in upper case
        '''
        list_name[i] = list_name[i][0].upper() + "."

    '''
    Finally joining the First and middle name using a whitespace sep.
    '''
    final_name = " ".join(list_name)
    print(final_name)

main()