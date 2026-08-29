def main():
    email = input("Enter your email: ")

    # Edge Case: Checking if its a valid email
    if '@' in email: # An email is valid only if it contains an '@' character
        '''
        #? .split() splits a string into list of substrings based on the sep(defaults to space)
        If it's valid, then split it up using '@' as the sep
        and then access the second element of the list.
        '''
        stripped = email.split('@')
        print(stripped[1])
    else:
        print("Invalid Email")
main()