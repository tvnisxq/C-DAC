from typing import Dict
from line import line
class InvalidPhoneNumberError(Exception):
    pass

def main():
    """
        CLI Contact Registry Interface
        1. #* Functions:
           -> def add_contact():
                #* Variables:
                    1. phonebook
                    2. name
                    3. phone_input

            -> def lookup_phone_input():
                #* Variables
                    1. phonebook
                    2. name

            -> def remove_contact():
                #* Variables
                1. phonebook
                2. name    
    """             

    contacts = {}
    contacts = register_contact(contacts, "Alice", "9131366969")
    contacts = register_contact(contacts, "Ghost", "7470495088")
    print(contacts)
    line()

    result = lookup_phone_input(contacts, "Alice")
    print(f"The contact number for Alice is: {result}")
    line()

    result = lookup_phone_input(contacts, "Ghost")
    print(result)
    line()

    print(processed_name("Alice"))
    line()
    print(processed_name("Bob123"))
    line()
    print(processed_name(""))
    line()
    print(processed_name("   "))
    line()
    print(processed_name("Mary Jane"))
# main()



def register_contact(phonebook: Dict[str, str], name: str, phone_input: str) -> Dict: 
    cleaned_name, is_valid = processed_name(name)

    # if not is_valid: raise ValueError with custom message
    if not is_valid:
        raise ValueError("Contact name must be a non-empty alphabetic string.")
            
    try: 
        int(phone_input)
    except ValueError: 
        raise InvalidPhoneNumberError("Phone number must contain digits only.")
    phonebook[name] = phone_input
    return phonebook

# register_contact()


# HELPER  
#* processed_name() is used as a helper function for register_contact() to validate contact names
def processed_name(name: str) ->  None:
    name = name.strip()
    letters_spaces = bool(name) and all(c.isalpha() or c.isspace() for c in name)
    return name, letters_spaces


#? lookup_phone_input is used to check if a contact is associated with a name
def lookup_phone_input(phonebook: Dict[str, str], name: str) -> str:
    return phonebook.get(name, "Contact not found!")
   
# lookup_phone_input()

def valid_phone_input(phonebook: Dict[str, str], name: str, phone_input: str) -> None: 
    ...
    contact_number = int(phone_input)



if __name__ == "__main__":
    main()