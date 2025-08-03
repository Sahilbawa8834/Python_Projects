def key_shift_cipher(message, key, direction):
  key_index = 0
  result = ''
  alphabet = "abcdefghijklmnopqrstuvwxyz"

  for char in message.lower():
    if char.isalpha():
      key_char = key[key_index % len(key)]
      key_index += 1

          # Convert key character to a shift (offset)
      offset = alphabet.index(key_char)
      index = alphabet.find(char)
      new_index = (index + offset * direction) % len(alphabet)
      result += alphabet[new_index]
    else:
      result += char
  return result 

# Testing the function
print(key_shift_cipher("hello world", "python", 1))