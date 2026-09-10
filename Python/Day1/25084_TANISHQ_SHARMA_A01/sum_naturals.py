def main():
    num = int(input("Enter a number: "))

    # Edge case handling negative or zero
    if num < 1:
        print("Invalid number! Please try again")

    ans = num * (num + 1) // 2
    print(ans)
    
main()