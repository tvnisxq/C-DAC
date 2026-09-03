def is_leap_year(year):
    """Determines if a year is a leap year using standard rules."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def validate_and_format_date(date_str):
    """
    Validates a 'DD/MM/YYYY' string without built-in date libraries
    and formats it into 'MonthName DD, YYYY' if valid.
    """
    # Manually split the date string by '/'
    parts = date_str.split('/')
    if len(parts) != 3:
        return "Invalid Date"

    # Ensure parts can be safely converted to integers
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except ValueError:
        return "Invalid Date"

    # Validate month range (1 to 12)
    if month < 1 or month > 12:
        return "Invalid Date"

    # Determine maximum days for the specific month
    if month in (4, 6, 9, 11):  # April, June, September, November
        max_days = 30
    elif month == 2:  # February leap year rules
        max_days = 29 if is_leap_year(year) else 28
    else:  # January, March, May, July, August, October, December
        max_days = 31

    # Validate day range for the specific month
    if day < 1 or day > max_days:
        return "Invalid Date"

    # Custom tuple of month names
    month_names = (
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    )

    # Return formatted long-form layout
    return f"{month_names[month - 1]} {day}, {year}"


if __name__ == "__main__":
    user_input = input("Enter a date string (DD/MM/YYYY): ")
    result = validate_and_format_date(user_input)
    print(result)