def alphabet_shift(custom_alphabet_lower, custom_alphabet_upper, input_string, shift):
    result = ''
    for char in input_string:
        if char in custom_alphabet_lower:  # Check if the character is lowercase
            index = custom_alphabet_lower.find(char)
            new_index = (index + shift) % len(custom_alphabet_lower)
            result += custom_alphabet_lower[new_index]
        elif char in custom_alphabet_upper:  # Check if the character is uppercase
            index = custom_alphabet_upper.find(char)
            new_index = (index + shift) % len(custom_alphabet_upper)
            result += custom_alphabet_upper[new_index]
        else:
            result += char  # Leave non-alphabetic characters unchanged
    return result

# Example usage
custom_alphabet_lower = "zyxwvutsrqponmlkjihgfedcba"
custom_alphabet_upper = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
input_string = "AbC XyZ"
shift = 3

print(alphabet_shift(custom_alphabet_lower, custom_alphabet_upper, input_string, shift))