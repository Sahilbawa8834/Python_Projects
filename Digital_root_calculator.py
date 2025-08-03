number = int(input("Enter the number you want to find the digital root for: "))

def digital_root(number):
	if number < 0:
		return False, "Invalid input. Please try again."
	
	# Calculate the digital root
	while number >= 10:
		total = 0
		for digit in str(number):
			total += int(digit)
		number = total
	return number

result = digital_root(number)
if isinstance(result, int):  # Check if the result is a valid integer
	print(f"The digital root of the input number is: {result}")
else:
	print(result[1])  # Print the error message if input is invalid

