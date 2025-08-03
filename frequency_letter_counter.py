def letter_frequency(message):
    freq = {}
    for char in message.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

# Testing the function
sample_text = "Hello World!"
print(letter_frequency(sample_text))
