def main():
    num = int(input("Enter a number: "))

    while True:
        if num <= 1:
            if num == 1:
                print("Invalid Number! Please retry")
            continue
        else:
            limit = num // 2
            div = 2 

            while div <= limit:
                if num % div == 0:
                    print(f"{num} is not a Prime Number as it is divisible by {div}")
                    break
                div += 1
            else:
                print(f"{num} is a Prime Number")
        break

main()