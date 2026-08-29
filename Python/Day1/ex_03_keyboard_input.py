def main():
    name = input("What's your name: ")
    city = input("Whats your city: ")

    print(f"Hello {name}, how's the weather in {city}?")

    age = int(input("What's your age? "))
    print(f"Ok, So you are {age} years old!")
    future_age = age + 10
    print(f"So after a decade, you'll be " + str(future_age) + " years old.")

main()