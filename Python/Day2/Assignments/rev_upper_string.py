def main():
    string = input("Enter a String: ")

    # Using slicing to reverse the string, chained with .upper() to make it all caps
    reversed_upper = string[::-1].upper()
    print(reversed_upper)

main()