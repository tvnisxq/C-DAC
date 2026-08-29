def main():
    sentence = input("Enter a Sentence: ")

    total_chars = len(sentence)
    print(f"The Total characters in the input Sentence is: {total_chars}")

    # split(): splits a string into a list of substrings based on the separator(defaults to spaces).
    word_count = len(sentence.split())
    print(f"The number of words in the input Sentence is: {word_count}")

main()