def main():
    age  = int(input("What's your age? "))

    if age >= 18:
        print("You can and should vote")

    else:
        if 18 - age == 1:
            print(f"You are under age. Wait for a year")
            
        else:
            print(f"You are under age. Wait for {18 - age} years")

main()