def vigenere_cipher(message, key, direction):
    key_index = 0
    result = ''
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.lower()  # Convert key to lowercase for consistency

    for char in message:
        if char.isalpha():  # Check if the character is alphabetic
            key_char = key[key_index % len(key)]  # Cycle through the key
            key_index += 1  # Increment key index only for alphabetic characters
            offset = alphabet_lower.index(key_char)  # Get the shift from the key

            if char.islower():  # Handle lowercase letters
                index = alphabet_lower.index(char)
                new_index = (index + offset * direction) % len(alphabet_lower)
                result += alphabet_lower[new_index]
            elif char.isupper():  # Handle uppercase letters
                index = alphabet_upper.index(char)
                new_index = (index + offset * direction) % len(alphabet_upper)
                result += alphabet_upper[new_index]
        else:
            result += char  # Leave non-alphabetic characters unchanged

    return result

# Example usage
message = input('enter the message you want to cipherer:  ')
key = input("Enter the key by which you want to encrypt the ciphere: ")
print("Encrypted:", vigenere_cipher(message, key, 1))  # Encryption
print("Decrypted:", vigenere_cipher("Wlqvq Cqvzf!", key, -1))  # Decryption