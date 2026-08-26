def main():
    name = input("What's your name? ")
    name = name.strip()

    city = input("Where are you from? ")
    city = city.strip()

    '''
    Strip function is used to tackle whitespaces.
    It strips away the whitespaces(both trailing and leading).
    '''
    if name == "": 
        name = "friend"

    '''
    len tells us the length of an object.
    Here we combine len with strip:
    
    1. city.strip() strips away all the whitespaces
    2. then len checks if the length of the string equates to zero
       -> if it does, city is replaced by "your city"
       -> if it doesn't, it prints the city being input by the user.
    '''
    if len(city) == 0:
        city = "your city"


    print(f"Hello {name}, how's weather in {city}?")


main()

