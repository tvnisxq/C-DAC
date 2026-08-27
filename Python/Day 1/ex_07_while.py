"""
This is an example script to understand the use of 'while' loops

Accept a number from the user and check if it is a prime or not
"""
def main():

    # Running an infinite loop and only breaking when the condition is met
    while True:
        num = int(input("Enter a number: "))
        if num < 1:
            print("Invalid number! Please retry")
            continue

        else:
            limit = num // 2
            div = 2

            while div <= limit:
                if num % div == 0:
                    print(f"{num} is not a Prime Number as it is divisible by {div}")
                    break
                d += 1
        break


main()