def main():
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))

    if year < 1:
        print("Invalid Year!")
        return

    if month < 1 and month > 12:
        print("Invalid month. Please enter a value between 1 to 12")

    if month == 2:
        max_days = 29 if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 28

    elif month in (4, 6, 9, 11):
        max_days = 30

    else:
        max_days = 31

    print(f"{month}/{year} has {max_days} maximum days")
    

main()