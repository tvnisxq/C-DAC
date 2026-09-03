sentence = input("Enter a sentence: ")

# Split the sentence into individual words
words = sentence.split()

# Reverse each word using list comprehension
reversed_words = [word[::-1] for word in words]

# Join the reversed words back into a sentence
result = " ".join(reversed_words)

print(result)
