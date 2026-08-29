# This is a function declaration
def main():
    print("This is a program to understand printing in python\n")

    name , city = "Tanishq", "Bangalore"
    print(name + " lives in " + city + ".\n")

    temp = 24
    '''
    This will result in TypeError: Can only concatenate Str(not int) with type str
    '''
    # print("In" + city + ", temperature tody is" + temp + "degrees")

    # Corrected Form(Using TypeCasting)
    print("In " + city + ", temperature today is " + str(temp) + " degrees")

    #? A couple of different ways to print this
    '''
    This is called an f-string or formatted-strings or even
    Doc Strings used mainly for documentation purpose.
    '''
    print(f"In {city}, temperature today is {temp} degrees") 

    '''
    C lang style printing, using %s to print strings and %d for integers/digits,
    similarly %f for float values
    '''
    print("In %s, temperature today is %d degrees" %(city, temp)) 

    '''
    Format string syntax:
    {0} and {1} are positional placeholders that get replaced 
    with arguments passed in the .format() in order
    '''
    print("In {0}, temperature today is {1} degrees\n".format(city, str(temp)))

    print(f"{name=}")
    print(f"{city=}")
    print(f"{temp=}\n")

    print('name =', name )
    print('city')
    print('temp')



# This is a function call
main()
