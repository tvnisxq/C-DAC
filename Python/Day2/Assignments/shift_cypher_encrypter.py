def main():
    string = input("Enter a String: ")
    shifter = int(input("Enter the Shift integer: "))

    # Created a placeholder for all the ascii characters
    charlist = []

    
    for char in string:
        '''
        we also need to first get the ord(char) because we are performing an
        addition with an int here(shifter) so the other value must also be an int.

        Then we convert it into chr() to get its ascii character(for e.g., chr(97) = 'a')

        we append the chr(ord(current_char) + 3) if the character
        is either lowercase or uppercase(This removes the special Characters)
        '''
        if char.islower():
            alph_pos = ord(char) - ord('a') # Find char position
            shifted_pos = (alph_pos + shifter) % 26 # Wraparound
            ascii_val = shifted_pos + ord('a') # ascii_val is the ascii code
            charlist.append(chr((ascii_val))) # we find the char for ascii_val to append it to char_list and append it

        # Same flow is followed for Uppercase Characters
        # We just perform the wraparound with ord('A')
        elif char.isupper():
            alph_pos = ord(char) - ord('A') 
            shifted_pos = (alph_pos + shifter) % 26
            ascii_val = shifted_pos + ord('A')
            charlist.append(chr((ascii_val)))

        # Every other character gets appended unchanged
        else:
            charlist.append(char)
    # .join() is then used to join the list of characters(using "" as the separtor)
    print("".join(charlist))
    # print(ord('a'))
main()