sample = "HelloWorld" #this is the sample 
def frequency(message): # function is defined
  freq ={} # empty dictionary 
  for char in message:
    if char.isalpha():
      freq[char] = freq.get(char, 0) + 1 # this will 
  return freq
freq = frequency(sample)

sorted_keys = sorted(freq.keys())

print("Letter | Frequency")
print("------------------")


for key in sorted_keys:
  print(f"{key} | {freq[key]}")
