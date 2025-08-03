def even_odd_classifier(numbers):
	for number in numbers:
		if numbers % 2 == 0:
			print(f"{numbers} is Even number")
		else:
			print(f"{numbers} odd number")

#testing
numbers = [1,2,3,4,5,6,7,8,9]
print(even_odd_classifier(numbers))
