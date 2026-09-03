def compress_string(text):
    """
    Compresses a string using run-length encoding (e.g., 'aabcccccaaa' -> 'a2b1c5a3').
    Returns the original string if the compressed version is not smaller.
    """
    if not text:
        return text

    compressed_chars = []
    count = 1

    # Iterate through the string starting from the second character
    for i in range(1, len(text)):
        # If the current character matches the previous one, increment the count
        if text[i] == text[i - 1]:
            count += 1
        else:
            # Append the previous character and its accumulated count to the list
            compressed_chars.append(f"{text[i - 1]}{count}")
            # Reset count for the new character sequence
            count = 1

    # Append the final character and its count after the loop ends
    compressed_chars.append(f"{text[-1]}{count}")
    
    # Combine the list into a single string
    compressed_text = "".join(compressed_chars)

    # Return the compressed string only if it is shorter than the original
    return compressed_text if len(compressed_text) < len(text) else text


if __name__ == "__main__":
    user_input = input("Enter a text string: ")
    result = compress_string(user_input)
    print(result)