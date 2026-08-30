def main():
    parent_string = input("Enter a string: ")
    sub_string = input("Enter a substring: ")

    # Taking the length of the substring
    sub_len = len(sub_string)

    # Starting by initializing a counter
    count = 0

    '''
    The last valid index here is index 4. Cuz 4th index is the last 
    index reaching where we still have two characters to check(index 4 and 5).
    So the range is (len(parent_string) - len(substring)) -> 6-2=4
    But since python's range excludes the element at last index,
    we add 1 to the range to reach at index 4 as the final iteration

    Banana
    012345
    '''
    for i in range(len(parent_string) - len(sub_string) + 1):
        # 1. Banana[0:2] = 'Ba' ; 'Ba' != 'an'
        # 2. Banana[1:3] = 'an' ; 'an' == 'an'
        # 3. Banana[2:4] = 'na' ; 'na' != 'an'
        # 4. Banana[3:5] = 'an' ; 'an' == 'an'
        # 5. Banana[4:6] = 'na' ; 'na' != 'an'
        # If that sliced chunk equates to the sub_string. We found one, and then we increment the count
        if parent_string[i : i + len(sub_string)] == sub_string:
            count += 1

    print(count)

main()