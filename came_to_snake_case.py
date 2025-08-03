### to create a function that takes a camel or pascal string and converts it to snake string which means camel is like this helloWorld pascal is like this HelloWorld and snake is like this hello_world
#creating the function 
message = 'TheWorldIsMine'
def snake_case_convertor(message):
	snake_list = ['_'+char.lower() if char.isupper() and index != 0 else char.lower() for index, char in enumerate(message)]
#join the list to form the final snake_case string 
	snake_case = ''.join(snake_list)
	return snake_case

# Test the function with different cases.
test1 = "CamelCaseExample"
test2 = "PascalCaseExample"
test3 = "thisIsCamelCase"
test4 = "AnotherExampleTest"

print("Original:", test1, "=> Snake Case:", snake_case_convertor(test1))
print("Original:", test2, "=> Snake Case:", snake_case_convertor(test2))
print("Original:", test3, "=> Snake Case:", snake_case_convertor(test3))
print("Original:", test4, "=> Snake Case:", snake_case_convertor(test4))


