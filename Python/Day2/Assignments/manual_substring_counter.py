def main():
    parent_string = input("Enter a string: ")
    sub_string = input("Enter a substring: ")

    # Taking the length of the substring
    sub_len = len(sub_string)

    # sub_string_count = defaultdict(int)
    count = 0
    for i in range(len(parent_string) - len(sub_string) + 1):
        if parent_string[i : i + len(sub_string)] == sub_string:
            count += 1

    print(count)
        



# 
# an

main()