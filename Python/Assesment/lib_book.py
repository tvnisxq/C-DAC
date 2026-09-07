#====================================================================================#
                        # Library Book Management System
#====================================================================================#

#---------------------------Validations----------------------------------------------

# Keep asking the user until they enter some valid value(non-empty string)
def get_text():
    while True:
        value = input("Enter the message: ").strip()

        # returns value when non empty string is entered
        if value != "":
            return value

        else:
            print("Enter a valid value! ")



def get_price():
    while True:
        price = float(input("Enter the price: "))

        if price > 0.0:
            return price

        else:
            print("price must be greater then 0 or positive number.")


def get_copies():
    while True:
        copies = int(input("Enter the no. of copies : " ))
        if copies >= 0:
            return copies

        else:
            print("copies must be an integer")




        
        











def main():
    ...
if '__name__'=="__main__":
    main()